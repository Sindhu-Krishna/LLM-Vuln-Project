# app.py (Flask)
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
log = logging.getLogger(__name__)

USERS = {"alice": "secret123"}

GENERIC_AUTH_ERROR = "Invalid credentials"

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Secure: Do not reveal user existence or internal details
    if not username or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Single generic failure response
    if username not in USERS or USERS[username] != password:
        # Log details server-side for investigation
        log.info("Auth failed for user '%s'", username)
        return jsonify({"error": GENERIC_AUTH_ERROR}), 401

    return jsonify({"message": "Logged in successfully"})
