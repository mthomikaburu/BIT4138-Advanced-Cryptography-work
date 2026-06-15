# cipher_test.py
from collections import Counter
from caesar_cipher import caesar_encrypt
from vigenere_cipher import vigenere_encrypt

def frequency_analysis(text):
    freq = Counter(text)
    for letter, count in freq.items():
        print(f"{letter}: {count}")

print("=== Testing Caesar Cipher ===")
cipher1 = caesar_encrypt("SECURITY", 4)
print("Cipher:", cipher1)
frequency_analysis(cipher1)

print("\n=== Testing Vigenère Cipher ===")
cipher2 = vigenere_encrypt("NETWORK", "KEY")
print("Cipher:", cipher2)
frequency_analysis(cipher2)
