# Secure Version (Path Validation)
import os

def read_file_secure(filename):
    base_path = "/var/app/data/"
    # Resolve absolute path and ensure it stays within base_path
    file_path = os.path.abspath(os.path.join(base_path, filename))
    if not file_path.startswith(os.path.abspath(base_path)):
        raise ValueError("Invalid file path!")
    with open(file_path, "r") as f:
        return f.read()
