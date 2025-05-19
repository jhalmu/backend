#!/bin/bash
set -e

# Aseta Python PATH
export PATH="/usr/local/bin:$PATH"

# Käynnistä IBKR Gateway taustalle
if [ -d "/app/gateway" ]; then
    cd /app/gateway && sh bin/run.sh root/conf.yaml &
    GATEWAY_PID=$!
    cd /app
else
    echo "Warning: Gateway directory not found, running in mock mode"
fi

# Odota että gateway on ylhäällä (tarkistetaan portti 5056)
for i in {1..12}; do
    if curl -s -f --connect-timeout 2 http://localhost:5056/v1/api/one/user/status > /dev/null 2>&1; then
        echo "Gateway is up!"
        break
    fi
    echo "Waiting for gateway... ($i/12)"
    sleep 5
done

# Käynnistä FastAPI-sovellus
if [ "$ENVIRONMENT" = "development" ]; then
    python -m uvicorn app:app --host 0.0.0.0 --port 5055 --reload --reload-dir /app
else
    python -m uvicorn app:app --host 0.0.0.0 --port 5055
fi

# Cleanup
if [ ! -z "$GATEWAY_PID" ]; then
    kill $GATEWAY_PID
fi 