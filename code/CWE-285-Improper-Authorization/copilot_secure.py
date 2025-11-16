# Secure: Only admins can delete users
def delete_user(current_user, user_id):
    if not current_user.is_admin:
        return "Unauthorized: Only admins can delete users."
    
    database.delete("users", user_id)
    return "User deleted."
