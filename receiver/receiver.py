from flask import Flask, request, jsonify
from datetime import datetime
import requests, os

app = Flask(__name__)

STORE_API_URL = os.environ.get("STORE_API_URL", "http://127.0.0.1:5001/store")

@app.route("/")
def index_page():
    return "Started <b>Receiver</b> server!"

@app.route("/message", methods=["POST"])
def transform_message():
    
    data = request.get_json()
    
    transformed_data = {
        "msg": data.get("message", ""),
        "dateTimeSent": datetime.now().isoformat()
    }

    try:
        response = requests.post(STORE_API_URL, json=transformed_data)
        if response.ok:
            storage_response = response.json()
            filename = storage_response.get("filename")
        
        storage_status = {
            "status": "success" if response.ok else "failed",
            "status_code": response.status_code,
            "filename" : filename
        }
    except requests.RequestException as e:
        storage_status = {
            "status": "failed",
            "error": str(e)
        }

    return jsonify(storage_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

