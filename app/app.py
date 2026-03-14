from flask import Flask, jsonify
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def home():
    return jsonify({"status": "running", "uptime": round(time.time() - start_time, 2)})

@app.route('/health')
def health():
    return jsonify({"healthy": True}), 200

@app.route('/metrics-test')
def metrics():
    return jsonify({"requests_served": 42}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)