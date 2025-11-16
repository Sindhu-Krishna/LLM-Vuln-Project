import os
from pathlib import Path

def load_file_secure(filename):
    """
    SECURE: Validates the final resolved path to prevent traversal.
    """
    base_dir = Path('/app/data/user_uploads/').resolve()
    
    # 1. Join the base directory and the user-supplied filename
    target_path = base_dir / filename
    
    # 2. Resolve the target path to get its absolute, canonical form 
    # (eliminating '..', '.', and symlinks)
    resolved_path = target_path.resolve()
    
    # 3. Check if the resolved path starts with the base_dir path
    if not str(resolved_path).startswith(str(base_dir)):
        raise ValueError("Attempted path traversal detected!")
    
    # Path is safe and within the designated directory
    file_path = resolved_path
    
    # In a real app, this line would open, read, or write to the file
    print(f"Attempting to load (SAFE): {file_path}")
    # file_data = open(file_path, 'r').read()
    return file_path

# Example of a malicious path input
malicious_path = "../../../etc/passwd"

try:
    load_file_secure(malicious_path)
except ValueError as e:
    print(f"ERROR: {e}")

# Example of a safe path input
safe_path = "document.pdf"
load_file_secure(safe_path)

# Output for malicious input: ERROR: Attempted path traversal detected!
# Output for safe input: Attempting to load (SAFE): /app/data/user_uploads/document.pdf
