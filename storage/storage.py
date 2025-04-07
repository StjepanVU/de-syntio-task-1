from flask import Flask, request, jsonify
from datetime import datetime
import os, random, string, json

app = Flask(__name__)

STORAGE_DIR = "stored_json"
os.makedirs(STORAGE_DIR, exist_ok=True)

@app.route("/")
def index_page():
    return "Started <b>Storage</b> server!"

@app.route("/storage/store", methods=["POST"])
def store_message():
    data = request.get_json()

    if not data or not isinstance(data, dict):
        return jsonify({
            "status": "failed",
            "error": "Invalid request: JSON data required"
        }), 400
    
    if "msg" not in data:
        return jsonify({
            "status": "failed",
            "error": "Invalid request: 'msg' field is required"
        }), 400
    
    if not data["msg"]:
        return jsonify({
            "status": "failed",
            "error": "Invalid request: 'msg' field cannot be empty"
        }), 400

    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    filename = f"msg-{random_string}.json"
    filepath = os.path.join(STORAGE_DIR, filename)

    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        return jsonify({
            "status": "failed",
            "error": f"Failed to store message: {str(e)}"
        }), 500

    return jsonify({
        "status": "success",
        "filename": filename
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
