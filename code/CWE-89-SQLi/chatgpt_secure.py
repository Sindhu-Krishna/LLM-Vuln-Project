# SECURE example — use parameterized queries / prepared statements
import sqlite3

def get_user_by_name(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # parameterized query: the DB library treats `?` as a placeholder
    cur.execute("SELECT id, username, email FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row

# Example call
# user = get_user_by_name("app.db", input("username: "))
