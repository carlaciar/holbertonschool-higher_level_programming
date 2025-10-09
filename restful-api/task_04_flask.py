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
    data = request.get_json(silent=True) or {}

    username = data.get("username")

    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "Username is required"}), 400

    username_key = username.strip()

    if username_key in users:
        return jsonify({"error": "Username already exists"}), 400
    
    data["username"] = username_key
    users[username_key] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


@app.route("/users/<username>", methods=["GET"])
def show_user(username):
    username_key = username.strip()
    if username_key in users:
        return jsonify(users[username_key])
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
