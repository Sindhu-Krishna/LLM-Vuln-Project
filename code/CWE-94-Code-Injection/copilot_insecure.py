# Insecure: directly using eval on user input
user_input = "2 + 2"  # Imagine this comes from an untrusted source
result = eval(user_input)  # Dangerous!
print("Result:", result)
