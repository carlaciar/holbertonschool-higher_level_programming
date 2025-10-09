#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    usernames = [user["username"] for user in users.values()]
    return (usernames)


@app.route('/users/<username>')
def show_user(username):
    for user_data in users.values():
        if user_data["username"] == username:
            return jsonify(user_data)


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({
        "message": f"User '{username}' added successfully!",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
