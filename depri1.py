import hashlib
from Crypto.Cipher import DES, ARC4
from Crypto.Random import get_random_bytes
import base64

# Hardcoded weak DES key (8 bytes)
DES_KEY = b"weakkey1"

# Hardcoded RC4 key
RC4_KEY = b"insecure_rc4_key"

def md5_hash(data):
    m = hashlib.md5()
    m.update(data.encode())
    return m.hexdigest()

def des_encrypt(data):
    cipher = DES.new(DES_KEY, DES.MODE_ECB)
    padded = data + (8 - len(data) % 8) * " "
    encrypted = cipher.encrypt(padded.encode())
    return base64.b64encode(encrypted)

def rc4_encrypt(data):
    cipher = ARC4.new(RC4_KEY)
    encrypted = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted)

if __name__ == "__main__":

    text = "SensitiveData"

    md5_value = md5_hash(text)
    print("MD5 Hash:", md5_value)

    des_value = des_encrypt(text)
    print("DES ECB Encryption:", des_value)

    rc4_value = rc4_encrypt(text)
    print("RC4 Encryption:", rc4_value)
