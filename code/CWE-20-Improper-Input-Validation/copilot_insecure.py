# INSECURE: No input validation
user_age = input("Enter your age: ")
age = int(user_age)   # Directly converting without checks
print(f"You are {age} years old.")
