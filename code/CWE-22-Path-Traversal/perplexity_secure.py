import os

# Secure: Validates input to prevent traversal
filename = os.path.basename(input("Enter filename:"))
filepath = f"/var/www/files/{filename}"
with open(filepath, "r") as f:
    print(f.read())
