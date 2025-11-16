# Insecure Example (CWE-94/Eval Injection)
user_input = "2 + 2"  # Pretend this comes from an untrusted source
# A malicious user could send something like:
# "os.system('rm -rf /')" or "__import__('os').system('cat /etc/passwd')"

try:
    # ⚠️ DANGEROUS: Executes arbitrary code as if it were part of the program.
    result = eval(user_input)
    print(f"Result: {result}")
except Exception as e:
    print(f"Error executing input: {e}")
