def rc4_init(key):
    """Key Scheduling Algorithm (KSA)"""
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_generate(S, n):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = j = 0
    keystream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream

def rc4_encrypt(key, plaintext):
    S = rc4_init(key)
    keystream = rc4_generate(S, len(plaintext))
    cipher = [ord(p) ^ k for p, k in zip(plaintext, keystream)]
    return bytes(cipher)

def rc4_decrypt(key, ciphertext):
    S = rc4_init(key)
    keystream = rc4_generate(S, len(ciphertext))
    plain = [c ^ k for c, k in zip(ciphertext, keystream)]
    return "".join(chr(p) for p in plain)

# Example run
key = "SECRET"
plaintext = "World Cup"
cipher = rc4_encrypt(key, plaintext)
decrypted = rc4_decrypt(key, cipher)

print("Plaintext:", plaintext)
print("Ciphertext (bytes):", cipher)
print("Decrypted:", decrypted)
