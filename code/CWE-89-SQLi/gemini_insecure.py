# INSECURE CODE (CWE-89: SQL Injection)
import sqlite3

def get_user_data_insecure(user_id):
    # DANGER: Directly injecting user_id into the query string
    # If user_id = "105 OR 1=1 --", the query becomes:
    # "SELECT * FROM users WHERE id = 105 OR 1=1 --;"
    query = "SELECT * FROM users WHERE id = " + user_id
    print(f"Insecure Query: {query}")
    # cursor.execute(query) # Operational call would be here
    return query
