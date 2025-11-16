# SECURE example (improved)
import os, base64, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Read key from environment (set this in a secret manager, not checked into source)
# Expect a 256-bit key encoded in base64: export MY_APP_KEY="$(python -c 'import os,base64; print(base64.b64encode(os.urandom(32)).decode())')"
b64_key = os.environ.get("MY_APP_KEY")
if not b64_key:
    raise RuntimeError("Missing encryption key in MY_APP_KEY (use env / secret manager)")

key = base64.b64decode(b64_key)
if len(key) not in (16, 24, 32):
    raise RuntimeError("Key length must be 128/192/256 bits")

aesgcm = AESGCM(key)
nonce = secrets.token_bytes(12)          # unique nonce for each encryption (recommended 12 bytes for AESGCM)
plaintext = b"Very sensitive data!!!"
aad = b"file-metadata"                   # optional additional authenticated data

ct = aesgcm.encrypt(nonce, plaintext, aad)
# store nonce + ct together (nonce is not secret but must be unique)
payload = base64.b64encode(nonce + ct).decode()
print("encrypted:", payload)
