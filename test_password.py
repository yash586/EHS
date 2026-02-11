# test_password.py
from security.password import hash_password, verify_password

plain = "secret"
hashed = hash_password(plain)
print("Hashed:", hashed)

assert verify_password("secret", hashed)
assert not verify_password("wrongpass", hashed)
print("✅ Password hashing works!")
