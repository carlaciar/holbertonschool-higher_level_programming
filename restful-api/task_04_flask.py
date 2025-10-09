#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    usernames = [user["username"] for user in users.values()]
    return (usernames)


@app.route("/data", methods=["GET"])
def data():
    return jsonify({"users": list(users.keys())})


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": f"User '{username}' added successfully!",
        "user": data
    }), 201


@app.route("/users/<username>", methods=["GET"])
def show_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
