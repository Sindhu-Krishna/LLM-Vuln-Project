def delete_user(user_id):
    # No authorization check - any logged-in user can call this!
    database.delete_user_by_id(user_id)
    return "User deleted"
