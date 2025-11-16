import os

# Insecure: directly concatenating user input into a system command
filename = input("Enter filename to list: ")
os.system("ls " + filename)  # Vulnerable to command injection
