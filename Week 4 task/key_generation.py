from Crypto.Random import get_random_bytes

key_128 = get_random_bytes(16)  # 128-bit
key_192 = get_random_bytes(24)  # 192-bit
key_256 = get_random_bytes(32)  # 256-bit

print("AES-128 Key:", key_128.hex())
print("AES-192 Key:", key_192.hex())
print("AES-256 Key:", key_256.hex())
