import logging # Assume logging is configured for internal use

try:
    # Attempt to load a configuration file based on user input 'config_name'
    file_path = f"/etc/app/configs/{config_name}.json"
    with open(file_path, 'r') as f:
        data = f.read()
    print("Configuration loaded.")

except FileNotFoundError as e:
    # ✅ SECURE: Log the detailed error internally for debugging
    logging.error(f"Configuration file access failure: {e}") 
    
    # ✅ SECURE: Provide the user with a generic, safe error message
    print("Error: The requested configuration file could not be loaded. Please check the name and try again.")
