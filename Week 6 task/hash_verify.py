import hashlib

message = b"ManchesterCity2026"
hash1 = hashlib.sha256(message).hexdigest()
hash2 = hashlib.sha256(message).hexdigest()

print("[OK] Hash1:", hash1)
print("[OK] Hash2:", hash2)
print("[OK] Verification:", hash1 == hash2)
