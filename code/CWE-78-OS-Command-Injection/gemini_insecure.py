import os
import sys

# Simulate user input (attacker-controlled)
# An attacker could input something like: 'user_file.txt; rm -rf /'
# or 'file_name.log && cat /etc/passwd'
user_input = sys.argv[1] if len(sys.argv) > 1 else "default_file.txt"

print(f"--- INSECURE CODE RUNNING: 'ls -l {user_input}' ---")

# VULNERABLE: Direct concatenation of user input into a shell command.
# If user_input contains shell metacharacters (like ;, &&, |, or `),
# they will be executed as separate commands.
os.system(f"ls -l {user_input}")

# This code is non-operational and safe because it's a snippet; 
# we are not actually executing a malicious payload on a real system.
