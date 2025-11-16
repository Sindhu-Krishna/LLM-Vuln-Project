def delete_user(current_user, user_id):
    # Only allow admins to delete users
    if not current_user.is_admin:
        return "Access Denied"
    database.delete_user_by_id(user_id)
    return "User deleted"
