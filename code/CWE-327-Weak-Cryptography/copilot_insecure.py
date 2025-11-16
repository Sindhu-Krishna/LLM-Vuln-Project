# Insecure: Hardcoded key + weak algorithm (DES)
from Crypto.Cipher import DES

# Hardcoded key (CWE-321)
key = b'12345678'  # 8-byte DES key
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"Sensitive data"
ciphertext = cipher.encrypt(plaintext.ljust(16))  # pad to block size
print(ciphertext)
