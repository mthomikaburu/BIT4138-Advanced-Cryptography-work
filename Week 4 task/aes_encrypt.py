# aes_encrypt.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len

key = get_random_bytes(16)  # 128-bit key
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b"BLOCKCIPHERDEMO"
ciphertext = cipher.encrypt(pad(plaintext))

print("Plaintext:", plaintext.decode())
print("Ciphertext (hex):", ciphertext.hex())
print("IV (hex):", cipher.iv.hex())
