from flask import Flask, request, jsonify
from datetime import datetime
import requests
import os

app = Flask(__name__)

STORE_API_URL = os.environ.get("STORE_API_URL", "http://127.0.0.1:5001/storage/store")

@app.route("/")
def index_page():
    return "Started <b>Receiver</b> server!"

@app.route("/receiver/message", methods=["POST"])
def transform_message():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "failed",
            "error": "invalid request"
        }), 400
    
    if set(data.keys()) != {"message"}:
        return jsonify({
            "status": "failed",
            "error": "invalid query"
        }), 400
    
    if not data.get("message"):
        return jsonify({
            "status": "failed",
            "error": "message cannot be empty"
        }), 400
    
    transformed_data = {
        "msg": data.get("message", ""),
        "dateTimeSent": datetime.now().isoformat()
    }
    
    storage_status = store_request(transformed_data)
    return jsonify(storage_status)

def store_request(transformed_data):
    storage_status = {
        "status": "failed",
        "status_code": None,
        "filename": None
    }
    
    try:
        response = requests.post(STORE_API_URL, json=transformed_data, timeout=10)
        storage_status["status_code"] = response.status_code
        
        if response.ok:
            try:
                storage_response = response.json()
                storage_status["status"] = "success"
                storage_status["filename"] = storage_response.get("filename")
            except ValueError:
                storage_status["error"] = "Invalid JSON response from storage service"
        else:
            storage_status["error"] = f"Storage service returned {response.status_code}"
            
    except requests.RequestException as e:
        storage_status["error"] = str(e)
    
    return storage_status

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
