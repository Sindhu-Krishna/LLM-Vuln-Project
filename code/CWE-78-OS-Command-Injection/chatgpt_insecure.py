# insecure_example.py  — non-operational illustration
# WARNING: this is intentionally insecure and should NOT be used in real code.

def list_remote_host_files(user_input):
    # user_input is inserted directly into a shell command (unsafe)
    cmd = "ssh user@" + user_input + " ls /tmp"
    # os.system invokes the shell; an attacker-controlled user_input can inject extra commands
    import os
    os.system(cmd)
