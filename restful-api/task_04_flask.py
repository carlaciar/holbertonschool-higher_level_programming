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
    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    normalised = username.strip().lower()

    if any(existing.lower() == normalised for existing in users):
        return jsonify({"error": "Username already exists"}), 400

    data["username"] = username.strip()
    users[username.strip()] = data

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
