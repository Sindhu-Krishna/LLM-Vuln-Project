def get_user_profile(user_id):
    try:
        # Simulate a database failure
        raise Exception("DB connection failed on host=10.0.12.6:5432 user=admin password=secret")
    except Exception as e:
        # ❌ Exposes internal system details and credentials
        return {"error": str(e)}
