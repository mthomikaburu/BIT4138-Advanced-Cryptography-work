# diffie_hellman.py

def diffie_hellman(p, g, a, b):
    # Generate public keys
    A = pow(g, a, p)   # User 1's public key
    B = pow(g, b, p)   # User 2's public key

    print(f"User 1 public key: {A}")
    print(f"User 2 public key: {B}")

    # Compute shared secrets
    secret1 = pow(B, a, p)  # User 1 computes secret
    secret2 = pow(A, b, p)  # User 2 computes secret

    print(f"User 1 secret: {secret1}")
    print(f"User 2 secret: {secret2}")

    # Verify
    if secret1 == secret2:
        print("✅ Shared secret established successfully!")
    else:
        print("❌ Secrets do not match!")

    return secret1


if __name__ == "__main__":
    print("=== Diffie-Hellman Key Exchange ===")

    # Public values
    p = int(input("Enter prime number p: "))
    g = int(input("Enter generator g: "))

    # Private keys
    a = int(input("Enter User 1 private key: "))
    b = int(input("Enter User 2 private key: "))

    shared_secret = diffie_hellman(p, g, a, b)
    print(f"\nFinal shared secret: {shared_secret}")
