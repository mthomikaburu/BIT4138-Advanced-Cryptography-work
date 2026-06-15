from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(private_key)

with open("encrypted_rsa.bin", "rb") as f:
    ciphertext = f.read()

plaintext = cipher.decrypt(ciphertext)
print("[OK] Decrypted message:", plaintext.decode())
