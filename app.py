app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Your GPT backend is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
