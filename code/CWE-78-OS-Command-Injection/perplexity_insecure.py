import os

# User input is unsanitized and passed directly to the shell
user_input = input("Enter filename to list: ")
os.system(f"ls {user_input}")
