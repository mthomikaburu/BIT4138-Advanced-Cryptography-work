# file_decrypt.py
from Crypto.Cipher import AES

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Step 1: Load AES key
with open("aes_key.bin", "rb") as f:
    key = f.read()

# Step 2: Load ciphertext
with open("encrypted.bin", "rb") as f:
    data = f.read()

iv = data[:16]
ciphertext = data[16:]

# Step 3: Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext))

# Step 4: Print result safely (no emoji)
print("[OK] Decrypted content:", plaintext.decode(errors="ignore"))
