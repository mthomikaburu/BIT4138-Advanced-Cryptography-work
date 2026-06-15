import bcrypt

password = b"LamineYamal"

# Generate salt and hash
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("[OK] Password Hash:", hashed.decode())
