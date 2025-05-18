#!/bin/bash
set -e

# Käynnistä IBKR Gateway taustalle
if [ -d "/app/gateway" ]; then
    cd /app/gateway && sh bin/run.sh root/conf.yaml &
    GATEWAY_PID=$!
    cd /app
else
    echo "Warning: Gateway directory not found, running in mock mode"
fi

# Odota että gateway on ylhäällä (tarkistetaan portti 5055)
for i in {1..12}; do
    if curl -k -s -f --connect-timeout 2 https://localhost:5055/v1/api/one/user/status > /dev/null 2>&1; then
        echo "Gateway is up!"
        break
    fi
    echo "Waiting for gateway... ($i/12)"
    sleep 5
done

# Käynnistä FastAPI-sovellus
exec uvicorn app:app --host 0.0.0.0 --port 5056 --reload 