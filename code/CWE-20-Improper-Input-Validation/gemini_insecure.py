import os

def load_file_insecure(filename):
    # DANGER: Directly using unvalidated user input
    # Imagine this function is part of a web server path handler.
    # The user could input "../../../etc/passwd"
    
    BASE_DIR = "/app/data/user_files/"
    full_path = BASE_DIR + filename
    
    print(f"Attempting to read: {full_path}")
    
    try:
        # A real application might open() and read the file here.
        # This print statement is a safe stand-in.
        print(f"Successfully processed file (simulated): {filename}")
        return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False

# Example of malicious input:
user_input_1 = "document.txt"
user_input_2 = "../../../system_config.ini"

print("--- Insecure Example ---")
load_file_insecure(user_input_1)
load_file_insecure(user_input_2) # This would attempt to read outside BASE_DIR in a real scenario
