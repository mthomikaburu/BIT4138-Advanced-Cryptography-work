from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(public_key)

message = b"Hello RSA secure transmission!"
ciphertext = cipher.encrypt(message)

with open("encrypted_rsa.bin", "wb") as f:
    f.write(ciphertext)

print("[OK] Message encrypted with public key.")
