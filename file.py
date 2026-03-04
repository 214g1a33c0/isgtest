import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Hardcoded secret key (for testing detection)
SECRET_KEY = b"0123456789abcdef"

def hash_password(password):
    sha = hashlib.sha256()
    sha.update(password.encode())
    return sha.hexdigest()

def encrypt_data(data):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode()))
    return base64.b64encode(cipher.iv + ciphertext)

def decrypt_data(enc):
    raw = base64.b64decode(enc)
    iv = raw[:16]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(raw[16:])
    return decrypted.strip()

def pad(data):
    while len(data) % 16 != 0:
        data += " "
    return data.encode()

if __name__ == "__main__":
    password_hash = hash_password("my_password")
    print("SHA256 Hash:", password_hash)

    encrypted = encrypt_data("Sensitive Data")
    print("Encrypted:", encrypted)

    decrypted = decrypt_data(encrypted)
    print("Decrypted:", decrypted)
