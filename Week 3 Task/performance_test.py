from rc4 import rc4_encrypt, rc4_decrypt
import time

key = "SECRET"
plaintext = "STREAMCIPHER" * 10000

start = time.time()
cipher = rc4_encrypt(key, plaintext)
end = time.time()
print("Encryption Time:", end - start, "seconds")

start = time.time()
decrypted = rc4_decrypt(key, cipher)
end = time.time()
print("Decryption Time:", end - start, "seconds")
print("Decryption successful:", decrypted == plaintext)
