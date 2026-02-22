from sklearn.ensemble import IsolationForest
import pandas as pd

def train_model():
    # Baseline safe operating data
    data = pd.DataFrame({
        "cpu_usage": [20, 30, 25, 35, 40, 28, 32],
        "memory_usage": [40, 45, 50, 55, 60, 48, 52],
        "disk_usage": [50, 55, 60, 58, 62, 57, 59]
    })

    model = IsolationForest(contamination=0.15)
    model.fit(data)
    return model


def predict_anomaly(model, metrics):
    # Use DataFrame to match training feature names
    data = pd.DataFrame([{
        "cpu_usage": metrics["cpu_usage"],
        "memory_usage": metrics["memory_usage"],
        "disk_usage": metrics["disk_usage"]
    }])

    return model.predict(data)