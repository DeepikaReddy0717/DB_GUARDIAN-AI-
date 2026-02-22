from flask import Flask, render_template, jsonify
from models.isolation_forest_model import train_model
from services.predictor_service import analyze_system

app = Flask(__name__)

model = train_model()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/metrics")
def get_metrics():
    result, metrics = analyze_system(model)

    alert_flag = bool(result[0] == -1)

    return jsonify({
        "cpu": float(metrics["cpu_usage"]),
        "memory": float(metrics["memory_usage"]),
        "disk": float(metrics["disk_usage"]),
        "timestamp": metrics["timestamp"],
        "alert": alert_flag
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
