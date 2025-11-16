# insecure_path_traversal.py (DO NOT USE IN PRODUCTION)
import os

def read_user_file(user_supplied_path):
    # Directly use user input to build a filesystem path
    with open(user_supplied_path, "r", encoding="utf-8") as f:
        return f.read()

# Example (unsafe) usage:
# contents = read_user_file(input_path_from_user)
