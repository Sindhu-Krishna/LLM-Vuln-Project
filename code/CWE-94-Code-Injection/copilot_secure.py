# Secure: safely parse and evaluate only expected expressions
import ast

user_input = "2 + 2"

try:
    # Parse input into an AST and only allow safe nodes
    tree = ast.parse(user_input, mode='eval')
    if all(isinstance(node, (ast.Expression, ast.BinOp, ast.Num, ast.Add, ast.Sub, ast.Mult, ast.Div))
           for node in ast.walk(tree)):
        result = eval(compile(tree, filename="<ast>", mode="eval"))
        print("Result:", result)
    else:
        print("Invalid expression")
except Exception:
    print("Invalid input")
