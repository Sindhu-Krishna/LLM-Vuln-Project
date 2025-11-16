import subprocess
import sys

# Simulate user input (attacker-controlled)
user_input = sys.argv[1] if len(sys.argv) > 1 else "default_file.txt"

print(f"--- SECURE CODE RUNNING: 'ls -l {user_input}' ---")

# SECURE: Using subprocess.run with the command and arguments as a list (shell=False by default).
# The user_input is treated ONLY as a single, literal argument to the 'ls -l' command, 
# even if it contains shell metacharacters.
try:
    subprocess.run(["ls", "-l", user_input], check=True)
except FileNotFoundError:
    print(f"Error: Command 'ls' not found or file access issue for '{user_input}'.")

# This code is non-operational and safe because it's a snippet.
