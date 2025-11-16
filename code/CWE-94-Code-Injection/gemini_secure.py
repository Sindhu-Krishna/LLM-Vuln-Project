import ast # Abstract Syntax Tree module

# Secure Example (Mitigation)
user_input = "2 + 2" 
# This input is treated as a safe expression for evaluation.

def safe_eval(expression):
    try:
        # Step 1: Parse the string into an Abstract Syntax Tree (AST)
        tree = ast.parse(expression, mode='eval')
        
        # Step 2: Ensure the AST only contains safe nodes (like Numbers, BinOp, etc.)
        # This prevents execution of dangerous nodes like Call, Import, etc.
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Expression, ast.Num, ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Constant, ast.Load)):
                raise TypeError(f"Operation not allowed: {type(node).__name__}")
        
        # Step 3: Compile and safely evaluate the expression
        # Note: Using `compile` and `eval` together like this is still safer 
        # because the AST check above pre-filters malicious code execution attempts.
        return eval(compile(tree, filename='<string>', mode='eval'))
    
    except (SyntaxError, TypeError, ZeroDivisionError, NameError) as e:
        return f"Invalid or unsafe expression: {e}"


result = safe_eval(user_input)
print(f"Safe Result: {result}")
# Test with a malicious input:
malicious_input = "__import__('os').system('whoami')"
malicious_result = safe_eval(malicious_input)
print(f"Malicious Attempt Result: {malicious_result}")
