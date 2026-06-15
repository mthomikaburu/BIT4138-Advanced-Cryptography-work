import bcrypt, time

password = b"World Cup 2026"


start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
end = time.time()

print("[OK] Hashing Time:", end - start, "seconds")

# Verification test
start = time.time()
bcrypt.checkpw(password, hashed)
end = time.time()

print("[OK] Verification Time:", end - start, "seconds")
