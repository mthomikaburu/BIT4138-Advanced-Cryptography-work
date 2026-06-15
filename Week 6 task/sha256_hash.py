import hashlib

message = b"World Cup 2026"
hash_value = hashlib.sha256(message).hexdigest()

print("[OK] SHA-256 Hash:", hash_value)
