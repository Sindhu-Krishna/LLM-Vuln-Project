import subprocess

# Secure: use subprocess with argument list (no shell=True)
filename = input("Enter filename to list: ")

# Example of basic validation: allow only alphanumeric filenames
if filename.isalnum():
    subprocess.run(["ls", filename])
else:
    print("Invalid filename")
