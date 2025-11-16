import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# 🛑 CWE-321: Hardcoded Key
HARDCODED_KEY = b"ThisIsAVerySecretHardcodedKey123" # Must be 32 bytes for AES-256

def encrypt_insecure(data):
    """Encrypts data using a hardcoded key."""
    cipher = AES.new(HARDCODED_KEY, AES.MODE_ECB)
    # Note: AES.MODE_ECB is also weak (CWE-327) but the primary focus here is the hardcoded key.
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(ct_bytes).decode('utf-8')

# Example usage
# encrypted = encrypt_insecure("Sensitive Data")
