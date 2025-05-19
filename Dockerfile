# syntax=docker/dockerfile:1
# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/
# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

# Build stage
FROM python:3.12-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim

# Create non-root user
#RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app 

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Create all necessary directories
RUN mkdir -p /app/gateway/logs \
    /app/gateway/root/cache \
    /app/static \
    /app/templates


# Copy IBKR Gateway and set up directories
RUN cd /app/gateway && \
    curl -O https://download2.interactivebrokers.com/portal/clientportal.gw.zip && \
    unzip clientportal.gw.zip && rm clientportal.gw.zip

# Copy application files
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY app.py mock_api.py start.sh db_config.py ./
COPY conf.yaml gateway/conf.yaml
COPY static/ static/
COPY templates/ templates/

# Set correct permissions and ownerships
RUN chown -R root:root /app && \
    # Set base permissions
    chmod -R 777 /app && \
    # Make start script executable
    chmod +x /app/start.sh && \
    # Set read-only permissions for Python and YAML files
    find /app -type f -name "*.py" -exec chmod 644 {} \; && \
    find /app -type f -name "*.yaml" -exec chmod 644 {} \; && \
    # Set write permissions for logs and cache directories
    chmod -R 777 /app/gateway/logs && \
    chmod -R 777 /app/gateway/root/cache

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV ENVIRONMENT=development

# Health check with more specific settings
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5055/health || exit 1

EXPOSE 5055 5056

# Switch to non-root user
USER appuser

CMD ["./start.sh"]