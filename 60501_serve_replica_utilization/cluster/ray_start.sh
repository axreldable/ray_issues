#!/bin/bash

#set -euo pipefail

# === CONFIG ===
LOG_DIR="logs"
mkdir -p "$LOG_DIR"
GRAFANA_LOG="$LOG_DIR/grafana.log"
RAY_LOG="$LOG_DIR/ray.log"
PROMETHEUS_LOG="$LOG_DIR/prometheus.log"

GRAFANA_CONFIG="/tmp/ray/session_latest/metrics/grafana/grafana.ini"
GRAFANA_PORT=3000
PROMETHEUS_PORT=9090
RAY_DASHBOARD_PORT=8265
HOST="http://localhost"

# === START RAY ===
echo "🟢 Starting Ray..." | tee -a "$RAY_LOG"
ray start --head > "$RAY_LOG" 2>&1
if [ ${PIPESTATUS[0]} -ne 0 ]; then
  echo "❌ Ray start failed. See error below:" | tee -a "$RAY_LOG"
  echo "🔻 Last 20 lines of $RAY_LOG:"
  tail -n 20 "$RAY_LOG"
  exit 1
fi

# === START PROMETHEUS ===
echo "🟢 Launching Prometheus..." | tee -a "$PROMETHEUS_LOG"
ray metrics launch-prometheus > "$PROMETHEUS_LOG" 2>&1

# === WAIT FOR GRAFANA CONFIG ===
echo "🟢 Waiting for grafana.ini to be generated..." | tee -a "$GRAFANA_LOG"
TIMEOUT=30
ELAPSED=0
while [ ! -f "$GRAFANA_CONFIG" ] && [ $ELAPSED -lt $TIMEOUT ]; do
    sleep 1
    echo "Waiting..."
    ELAPSED=$((ELAPSED + 1))
done

if [ ! -f "$GRAFANA_CONFIG" ]; then
    echo "❌ Timed out waiting for $GRAFANA_CONFIG" | tee -a "$GRAFANA_LOG"
    exit 1
fi

# === START GRAFANA ===
echo "✅ Starting Grafana server in background..." | tee -a "$GRAFANA_LOG"
nohup grafana server \
  --config="$GRAFANA_CONFIG" \
  --homepath="$(brew --prefix grafana)/share/grafana" \
  web >> "$GRAFANA_LOG" 2>&1 &

# === SERVICE URL OUTPUT ===
echo ""
echo "🎉 All services started successfully."
echo ""
echo "📍 Service Endpoints:"
echo "🔷 Ray Dashboard:    $HOST:$RAY_DASHBOARD_PORT"
echo "🔶 Prometheus:       $HOST:$PROMETHEUS_PORT"
echo "🟢 Grafana:          $HOST:$GRAFANA_PORT"
echo ""
echo "📝 Log files:"
echo "   • Ray:        $RAY_LOG"
echo "   • Prometheus: $PROMETHEUS_LOG"
echo "   • Grafana:    $GRAFANA_LOG"