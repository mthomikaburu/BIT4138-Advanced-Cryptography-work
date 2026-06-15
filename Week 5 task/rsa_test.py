from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time


with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

cipher_pub = PKCS1_OAEP.new(public_key)
cipher_priv = PKCS1_OAEP.new(private_key)

message = b"RSA performance test message"


start = time.time()
ciphertext = cipher_pub.encrypt(message)
end = time.time()
print("[OK] Encryption Time:", end - start, "seconds")

# Decryption timing
start = time.time()
plaintext = cipher_priv.decrypt(ciphertext)
end = time.time()
print("[OK] Decryption Time:", end - start, "seconds")
print("[OK] Validation:", plaintext.decode())
