import os
from pathlib import Path

def load_file_secure(filename):
    # FIX: Validate the input to ensure it stays within the intended directory
    
    BASE_DIR = Path("/app/data/user_files/").resolve()
    
    # 1. Construct the path
    potential_path = BASE_DIR / filename
    
    # 2. Canonicalize the path (resolving '..', '.', symlinks)
    try:
        resolved_path = potential_path.resolve(strict=False)
    except FileNotFoundError:
        # Handle cases where the path doesn't exist yet, if needed
        resolved_path = potential_path.resolve(strict=False).parent # Fallback logic

    print(f"Constructed path: {resolved_path}")

    # 3. Validation Check: Ensure the resolved path STARTS WITH the BASE_DIR
    if not str(resolved_path).startswith(str(BASE_DIR)):
        print(f"SECURITY ALERT: Attempted directory traversal detected for input '{filename}'.")
        return False
    
    # Input is now validated and safe to use
    print(f"Attempting to read SAFE file: {resolved_path}")
    
    try:
        # A real application would open() and read the file here.
        print(f"Successfully processed file (simulated): {filename}")
        return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False

# Example of malicious input:
user_input_1 = "document.txt"
user_input_2 = "../../../system_config.ini"

print("\n--- Secure Example ---")
load_file_secure(user_input_1)
load_file_secure(user_input_2) # This is now blocked by the validation check
