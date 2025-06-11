from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b'1234567890abcdef'  # 16 bytes key
iv = b'abcdef1234567890'   # 16 bytes IV

def encrypt_message(msg: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(msg.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_message(encoded: str) -> str:
    encrypted = base64.b64decode(encoded.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode('utf-8')