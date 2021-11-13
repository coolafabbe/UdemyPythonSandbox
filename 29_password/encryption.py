from cryptography.fernet import Fernet 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
import base64

class PasswordEncryption():
    def __init__(self, key, salt) -> None:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        self._key = base64.urlsafe_b64encode(kdf.derive(key))

    def encrypt(self, message):
        message = message.encode()
        f = Fernet(self._key)
        return f.encrypt(message)

    def decrypt(self, encrypted):
        return Fernet(self._key).decrypt(encrypted)

# key = input("Enter the key: ").encode()
# print(key)
# print(type(key))
# salt = b'SALT'
# print(salt)
# print(type(salt))
# kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=100000,
#         backend=default_backend()
#         )
# _key = base64.urlsafe_b64encode(kdf.derive(key))

# print(_key)

# message = "Hello world".encode()
# f = Fernet(_key) 
# encrypted = f.encrypt(message) 
# decrypted = f.decrypt(encrypted)

# print(encrypted)
# print(decrypted)




