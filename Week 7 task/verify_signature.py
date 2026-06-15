# digital_signature.py
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Save keys
with open("private.pem", "wb") as f:
    f.write(private_key.export_key())
with open("public.pem", "wb") as f:
    f.write(public_key.export_key())

# Message
message = b"Secure document content"
hash_obj = SHA256.new(message)

# Sign with private key
signature = pkcs1_15.new(private_key).sign(hash_obj)

with open("signature.bin", "wb") as f:
    f.write(signature)

print("[OK] Digital signature generated and saved.")
