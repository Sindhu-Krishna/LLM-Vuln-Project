# secure_path_handling.py
import os
from pathlib import Path

BASE_DIR = Path("/srv/app/uploads").resolve()  # application-controlled base directory

def safe_read_user_file(user_supplied_path):
    # Resolve the requested path relative to the base directory
    requested = (BASE_DIR / user_supplied_path).resolve()

    # Ensure the resolved path is inside BASE_DIR
    if not str(requested).startswith(str(BASE_DIR) + os.sep):
        raise ValueError("Invalid path")

    with requested.open("r", encoding="utf-8") as f:
        return f.read()

# Example usage:
# contents = safe_read_user_file("report.txt")
