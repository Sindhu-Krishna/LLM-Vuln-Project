# Insecure version: eval on untrusted input
def insecure_eval(user_input):
    # Dangerous: executes arbitrary code from user input
    return eval(user_input)

# Secure version: avoid eval, use a safe parser or whitelist allowed operations
def secure_eval(user_input):
    # Example: only allow simple arithmetic expressions using literal eval
    import ast
    import operator

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def eval_expr(node):
        if isinstance(node, ast.Expression):
            return eval_expr(node.body)
        elif isinstance(node, ast.BinOp):
            if type(node.op) in allowed_operators:
                return allowed_operators[type(node.op)](
                    eval_expr(node.left), eval_expr(node.right)
                )
            else:
                raise ValueError("Disallowed operator")
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise ValueError("Unsupported expression")

    try:
        expr_ast = ast.parse(user_input, mode='eval')
        return eval_expr(expr_ast)
    except Exception:
        return "Invalid expression"

# Example usage (Don't run insecure_eval with untrusted input):
# insecure_eval("__import__('os').system('rm -rf /')")  # Dangerous
# secure_eval("2 + 3 * 4")  # Returns 14
