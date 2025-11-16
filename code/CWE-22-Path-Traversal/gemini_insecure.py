import os

def load_file_insecure(filename):
    """
    INSECURE: Does not sanitize or validate 'filename'.
    Allows path traversal (e.g., filename='../../../etc/passwd').
    """
    # Simulate a web request or user input fetching a file
    base_dir = '/app/data/user_uploads/'
    
    # Path construction is the vulnerability point
    file_path = os.path.join(base_dir, filename)
    
    # In a real app, this line would open, read, or write to the file
    print(f"Attempting to load: {file_path}") 
    # file_data = open(file_path, 'r').read()
    return file_path

# Example of a malicious path input
malicious_path = "../../../etc/passwd"
load_file_insecure(malicious_path) 

# Output for malicious input: Attempting to load: /app/data/user_uploads/../../../etc/passwd
