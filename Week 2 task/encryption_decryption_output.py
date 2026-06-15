from caesar_cipher import caesar_encrypt, caesar_decrypt
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

print("=== Caesar Cipher ===")
plain1 = "SECURITY"
shift = 4
cipher1 = caesar_encrypt(plain1, shift)
print(f"Plain: {plain1} | Cipher: {cipher1} | Decrypted: {caesar_decrypt(cipher1, shift)}")

print("\n=== Vigenere Cipher ===")
plain2 = "NETWORK"
key = "KEY"
cipher2 = vigenere_encrypt(plain2, key)
print(f"Plain: {plain2} | Cipher: {cipher2} | Decrypted: {vigenere_decrypt(cipher2, key)}")
