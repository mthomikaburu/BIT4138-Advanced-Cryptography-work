def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Example usage
plaintext = "MKU"
shift = 4
ciphertext = caesar_encrypt(plaintext, shift)

print("Plaintext:", plaintext)
print("Shift:", shift)
print("Ciphertext:", ciphertext)
