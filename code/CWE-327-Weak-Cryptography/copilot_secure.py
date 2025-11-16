# Secure: Strong algorithm (AES) + environment-based key
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Load key from environment (not hardcoded)
key = os.environ.get("APP_SECRET_KEY")
if key is None:
    raise ValueError("APP_SECRET_KEY not set in environment")

# Ensure key is 32 bytes for AES-256
key = key.encode("utf-8")[:32].ljust(32, b'\0')

cipher = AES.new(key, AES.MODE_GCM)
plaintext = b"Sensitive data"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print(ciphertext, tag)
