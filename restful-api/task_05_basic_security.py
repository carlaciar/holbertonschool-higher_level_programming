#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from functools import wraps

# app name
app = Flask(__name__)

# token
app.config["access_token"] = "jwt_token123"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": werkzeug.security.generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": werkzeug.security.generate_password_hash("password"),
        "role": "admin"
    }
}


# ---------------------------
# BASIC AUTHENTICATION
# ---------------------------
@auth.verify_password
def verify_password(username, password):
    """Check if username and password are valid."""
    user = users.get(username)
    if not user:
        # invalid username
        return None
    if not check_password_hash(user["password"], password):
        # invalid password
        return None
    return username  # returning username means authentication success


@auth.error_handler
def basic_auth_error(status):
    """Return consistent 401 error for unauthorized access."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route using Basic Auth."""
    return "Basic Auth: Access Granted", 200


# ---------------------------
# JWT AUTHENTICATION
# ---------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON:
    {
        "username": "user1",
        "password": "password"
    }
    Returns:
    {
        "access_token": "<JWT_TOKEN>"
    }
    """
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        # Invalid credentials
        return jsonify({"error": "Invalid username or password"}), 401

    # Include the user's role in the JWT payload
    additional_claims = {"role": user["role"]}
    token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )

    return jsonify({"access_token": token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route using JWT token."""
    return "JWT Auth: Access Granted", 200


# ---------------------------
# ROLE-BASED ACCESS CONTROL
# ---------------------------
def role_required(*allowed_roles):
    """Decorator to restrict access by role (checks role claim in JWT)."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            role = claims.get("role")
            if role not in allowed_roles:
                # user has a valid token but not enough privileges
                return jsonify({"error": "Admin access required"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@app.route("/admin-only", methods=["GET"])
@jwt_required()
@role_required("admin")
def admin_only():
    """Admin-only route."""
    return "Admin Access: Granted", 200


# ---------------------------
# General error handling for JWT
# ---------------------------
@jwt.unauthorized_loader
def missing_token_callback(err):
    """Handles missing or invalid JWT tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(err):
    """Handles malformed JWT tokens."""
    return jsonify({"error": "Invalid token"}), 401


# ---------------------------
# Run the app
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
