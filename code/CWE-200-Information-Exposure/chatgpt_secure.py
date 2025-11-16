def get_user_profile(user_id):
    try:
        raise Exception("DB connection failed")  # Internal detail hidden
    except Exception:
        # ✅ Returns only generic message suitable for end-users
        return {"error": "Unable to complete your request at this time."}
