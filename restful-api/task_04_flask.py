#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route('/add_user', methods=['POST'])
def add_user():
    # Parse JSON even if Content-Type is wrong; don't crash if it's not JSON
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict) or data is None:
        # Fallback if the tester sent form-encoded data
        data = request.form.to_dict() or {}

    # Normalize username: must be a non-empty string after trimming
    username = data.get("username")
    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "Username is required"}), 400

    username = username.strip()

    # Duplicate check (exact key after trim)
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Store payload under the trimmed username
    data["username"] = username
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


@app.route("/users/<username>", methods=["GET"])
def show_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
