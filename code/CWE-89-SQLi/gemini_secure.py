# SECURE FIXED CODE (Using Prepared Statements)
import sqlite3

def get_user_data_secure(user_id):
    # SAFE: Using a parameter placeholder (?)
    query = "SELECT * FROM users WHERE id = ?"
    parameters = (user_id,)
    print(f"Secure Query Template: {query}")
    print(f"Parameters: {parameters}")
    # cursor.execute(query, parameters) # Operational call would be here
    return query, parameters
