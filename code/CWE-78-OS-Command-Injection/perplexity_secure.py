import subprocess

# The input is validated to only allow alphanumeric filenames
user_input = input("Enter filename to list: ")
if user_input.isalnum():
    subprocess.run(["ls", user_input])
else:
    print("Invalid filename.")
