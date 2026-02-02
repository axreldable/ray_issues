#!/bin/sh

LOG_DIR="logs"

echo "🔻 Stopping Ray cluster..."
ray stop

echo "🔻 Stopping Prometheus..."
ray metrics shutdown-prometheus

echo "🔻 Stopping Grafana..."
# Attempt to find and kill Grafana process started by our script
GRAFANA_PID=$(ps aux | grep "[g]rafana server" | awk '{print $2}')
if [ -n "$GRAFANA_PID" ]; then
    kill "$GRAFANA_PID"
    echo "✅ Grafana process $GRAFANA_PID terminated."
else
    echo "⚠️  No running Grafana process found."
fi

echo "🔻 Cleaning resources..."
rm -rf data prometheus*

echo ""
echo "🧹 Cleanup complete."
echo "📝 Check logs for details: $LOG_DIR"
