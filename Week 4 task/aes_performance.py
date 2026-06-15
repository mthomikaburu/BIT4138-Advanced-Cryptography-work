# aes_performance.py
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len

# Step 1: Generate key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Step 2: Create large plaintext for testing
plaintext = b"AESPERFORMANCE" * 100000  # ~1.3 MB

# Step 3: Encryption timing
cipher = AES.new(key, AES.MODE_CBC, iv)
start = time.time()
ciphertext = cipher.encrypt(pad(plaintext))
end = time.time()
print("[OK] Encryption Time:", end - start, "seconds")

# Step 4: Decryption timing
decipher = AES.new(key, AES.MODE_CBC, iv)
start = time.time()
decrypted = decipher.decrypt(ciphertext)
end = time.time()
print("[OK] Decryption Time:", end - start, "seconds")
