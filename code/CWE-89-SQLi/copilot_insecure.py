import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Insecure: directly concatenating user input into SQL
user_id = input("Enter user ID: ")
query = "SELECT * FROM users WHERE id = " + user_id
cursor.execute(query)  # Vulnerable to SQL Injection!
