import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 🗝️ Secure Key Handling
def get_encryption_key():
    """Retrieves key from environment variable or throws an error."""
    # The key should be generated securely and stored externally (e.g., in a secret manager).
    key = os.getenv("APP_ENCRYPTION_KEY")
    if not key or len(key.encode('utf-8')) != 32:
        raise ValueError("Encryption key not found or is not 32 bytes (for AES-256).")
    return key.encode('utf-8')

def encrypt_secure(data):
    """Encrypts data using a secure, externally managed key and GCM mode."""
    key = get_encryption_key()
    cipher = AES.new(key, AES.MODE_GCM) # Stronger GCM mode
    nonce = cipher.nonce # Initialization Vector (Nonce)

    data_bytes = data.encode('utf-8')
    ciphertext, tag = cipher.encrypt_and_digest(data_bytes)
    
    # Store Nonce, Ciphertext, and Tag for decryption
    return base64.b64encode(nonce + ciphertext + tag).decode('utf-8')

# Example setup (simulating an environment variable)
# os.environ["APP_ENCRYPTION_KEY"] = "ThisIsAStrong32ByteKeyForAES256!!"
# encrypted = encrypt_secure("Sensitive Data")
