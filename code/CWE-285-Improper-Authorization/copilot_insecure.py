# Insecure: Anyone can delete a user without authorization
def delete_user(user_id):
    # Directly deletes user without checking who is making the request
    database.delete("users", user_id)
    return "User deleted."
