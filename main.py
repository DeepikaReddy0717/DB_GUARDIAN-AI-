from models.isolation_forest_model import train_model
from services.predictor_service import analyze_system
import time

print("🚀 DB Guardian AI - Real-Time Monitoring Started")

model = train_model()

while True:
    result, metrics = analyze_system(model)

    print(f"""
    Time: {metrics['timestamp']}
    CPU Usage: {metrics['cpu_usage']}%
    Memory Usage: {metrics['memory_usage']}%
    Disk Usage: {metrics['disk_usage']}%
    """)

    if result[0] == -1:
        print("⚠️ ALERT: Potential Downtime Risk Detected!\n")
    else:
        print("✅ System Operating Normally\n")

    print("=" * 50)
    time.sleep(5)  # Runs every 5 seconds