# syntax=docker/dockerfile:1
# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/
# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7
FROM debian:bookworm-slim

# Päivitä paketit ja asenna tarvittavat työkalut
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y openjdk-17-jre-headless \
                       unzip curl procps vim net-tools \
                       python3 python3-pip python3.11-venv

WORKDIR /app

# Lataa ja pura IBKR gateway
RUN mkdir gateway && cd gateway && \
    curl -O https://download2.interactivebrokers.com/portal/clientportal.gw.zip && \
    unzip clientportal.gw.zip && rm clientportal.gw.zip

# Kopioi konfiguraatio ja käynnistysskripti
COPY conf.yaml gateway/root/conf.yaml
COPY start.sh /app/start.sh

# Kopioi sovellustiedostot
COPY app.py /app/
COPY mock_api.py /app/
COPY requirements.txt /app/
COPY static/ /app/static/
COPY templates/ /app/templates/

# Asenna Python-riippuvuudet
RUN pip3 install --break-system-packages -r requirements.txt

EXPOSE 5055 5056

CMD sh ./start.sh