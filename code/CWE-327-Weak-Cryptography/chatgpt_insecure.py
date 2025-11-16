# INSECURE example (do NOT use in real code)
from Crypto.Cipher import AES           # PyCryptodome
import hashlib

# Hardcoded secret (CWE-321)
HARD_CODED_KEY = b"my-secret-key-123"   # short, stored in source

# Weak choice: using MD5-derived key and AES in ECB mode (CWE-327)
key = hashlib.md5(HARD_CODED_KEY).digest()   # MD5 is broken; 128-bit key
cipher = AES.new(key, AES.MODE_ECB)          # ECB leaks structure, no IV

plaintext = b"Very sensitive data!!!   "     # must be block-aligned for ECB
ct = cipher.encrypt(plaintext)
print("ciphertext:", ct.hex())
