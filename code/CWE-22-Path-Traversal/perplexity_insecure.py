# Insecure: Directly uses user input in file path
filename = input("Enter filename:")
with open(f"/var/www/files/{filename}", "r") as f:
    print(f.read())
