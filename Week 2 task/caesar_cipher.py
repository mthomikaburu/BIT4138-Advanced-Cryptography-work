def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

# Example run
plaintext = "HELLO"
shift = 4
cipher = caesar_encrypt(plaintext, shift)
print("Plaintext:", plaintext)
print("Ciphertext:", cipher)
print("Decrypted:", caesar_decrypt(cipher, shift))
