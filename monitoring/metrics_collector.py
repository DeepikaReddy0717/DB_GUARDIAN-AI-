import psutil
import datetime

def collect_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    }
    return metrics