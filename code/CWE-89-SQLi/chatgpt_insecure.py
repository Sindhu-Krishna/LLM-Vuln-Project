# INSECURE example — do NOT use in production
import sqlite3

def get_user_by_name(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # unsafe: user input concatenated into SQL string
    query = "SELECT id, username, email FROM users WHERE username = '%s'" % username
    cur.execute(query)   # vulnerable to SQL injection
    row = cur.fetchone()
    conn.close()
    return row

# Example call (illustrative only)
# user = get_user_by_name("app.db", input("username: "))
