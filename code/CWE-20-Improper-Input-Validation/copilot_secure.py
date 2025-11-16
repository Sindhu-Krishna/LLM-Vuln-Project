# SECURE: Input validation added
user_age = input("Enter your age: ")

if user_age.isdigit():  # Check if input contains only digits
    age = int(user_age)
    if 0 <= age <= 120:  # Reasonable range check
        print(f"You are {age} years old.")
    else:
        print("Error: Age must be between 0 and 120.")
else:
    print("Error: Please enter a valid number.")
