#!/usr/bin/python3

from flask import Flask, jsonify
import werkzeug.security
from flask_httpauth import HTTPBasicAuth

# app name
app = Flask(__name__)

# authentication object
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return username  # returning username means "authentication success"
    return None  # returning None means "authentication failed"


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify("Basic Auth: Access Granted"), 200