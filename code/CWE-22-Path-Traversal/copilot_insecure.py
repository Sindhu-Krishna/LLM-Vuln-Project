# Insecure Version (Path Traversal Vulnerability)
import os

def read_file_insecure(filename):
    base_path = "/var/app/data/"
    file_path = os.path.join(base_path, filename)  # No validation
    with open(file_path, "r") as f:
        return f.read()

# Example exploit: filename = "../../etc/passwd"
