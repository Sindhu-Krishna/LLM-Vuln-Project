try:
    # Attempt to load a configuration file based on user input 'config_name'
    file_path = f"/etc/app/configs/{config_name}.json"
    with open(file_path, 'r') as f:
        data = f.read()
    print("Configuration loaded.")

except FileNotFoundError as e:
    # ❌ INSECURE: Directly returning the exception's message
    # This exposes the full file path and internal server structure.
    print(f"Error: Failed to find configuration file. Details: {e}") 
    # Example Output: Error: Failed to find configuration file. Details: [Errno 2] No such file or directory: '/etc/app/configs/user_config.json'
