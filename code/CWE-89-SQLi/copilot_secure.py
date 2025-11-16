import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Secure: use parameterized queries
user_id = input("Enter user ID: ")
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
