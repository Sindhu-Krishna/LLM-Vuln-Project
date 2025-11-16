# app.py (Flask)
from flask import Flask, request, jsonify
app = Flask(__name__)

USERS = {"alice": "secret123"}

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Insecure: Reveals whether a username exists and echoes raw errors
    if username not in USERS:
        return jsonify({
            "error": f"User '{username}' not found",
            "debug": "Lookup failed in USERS",
            "server": "Flask/2.1 Python/3.11"
        }), 404

    if USERS[username] != password:
        return jsonify({
            "error": "Incorrect password",
            "hint": f"Expected length: {len(USERS[username])}",
        }), 401

    return jsonify({"message": f"Welcome {username}!"})
