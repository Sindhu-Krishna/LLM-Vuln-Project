# INSECURE: executes untrusted code directly
user_input = input("Enter math expression: ")   # e.g. "2 + 3"
result = eval(user_input)                       # DANGEROUS
print("Result:", result)
