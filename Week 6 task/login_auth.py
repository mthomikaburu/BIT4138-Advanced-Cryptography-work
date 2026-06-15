import bcrypt

# Stored hash (from registration)
stored_hash = bcrypt.hashpw(b"MySecretPassword", bcrypt.gensalt())

# User login attempt
user_input = b"MySecretPassword"

if bcrypt.checkpw(user_input, stored_hash):
    print("[OK] Authentication Successful")
else:
    print("[FAIL] Authentication Failed")
