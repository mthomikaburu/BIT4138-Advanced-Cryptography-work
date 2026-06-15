def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in cipher.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

# Example run
plaintext = "LETS GO!"
key = "KEY"
cipher = vigenere_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", cipher)
print("Decrypted:", vigenere_decrypt(cipher, key))
