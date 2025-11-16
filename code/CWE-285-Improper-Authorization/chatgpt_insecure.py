# Flask-like pseudocode (minimal, non-operational)
from flask import request, jsonify

# Endpoint to delete a user (intended for admins) — NO authorization check
@app.route("/admin/delete_user/<user_id>", methods=["POST"])
def delete_user(user_id):
    # blindly deletes whichever user_id is passed
    db.delete_user(user_id)
    return jsonify({"status": "deleted", "user": user_id})
