# secure_example.py  — non-operational illustration

import subprocess
import ipaddress
import re

HOSTNAME_REGEX = re.compile(r"^[a-zA-Z0-9\-\.]{1,253}$")  # simple allowlist for hostnames

def is_valid_hostname(host):
    return bool(HOSTNAME_REGEX.fullmatch(host)) and len(host) <= 253

def is_valid_ip(addr):
    try:
        ipaddress.ip_address(addr)
        return True
    except ValueError:
        return False

def list_remote_host_files(user_input):
    # 1) Validate input — allow only safe hostnames or IPs
    if not (is_valid_hostname(user_input) or is_valid_ip(user_input)):
        raise ValueError("invalid host")

    # 2) Use subprocess with an argument list (no shell) to avoid shell interpretation
    # NOTE: using SSH still requires care (keys, escaping). This demonstrates avoiding shell injection.
    subprocess.run(["ssh", f"user@{user_input}", "ls", "/tmp"], check=True)
