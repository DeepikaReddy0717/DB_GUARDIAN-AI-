from monitoring.metrics_collector import collect_metrics
from models.isolation_forest_model import predict_anomaly
import csv
import os

CSV_FILE = "laptop_metrics.csv"

def analyze_system(model):
    metrics = collect_metrics()
    result = predict_anomaly(model, metrics)

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "cpu_usage", "memory_usage", "disk_usage"])

        writer.writerow([
            metrics["timestamp"],
            metrics["cpu_usage"],
            metrics["memory_usage"],
            metrics["disk_usage"]
        ])

    return result, metrics