import Crypto.Random
from Crypto.Cipher import AES
import hashlib

class AES256:
    def __init__(self):
        self.BLOCK_BIT_SIZE = 128
        self.KEY_BIT_SIZE = 256
        self.SALT_BIT_SIZE = 128
        self.ITERATIONS = 10000

    def encrypt(self, plainText, key):
        if key == None or key == "":
            raise ValueError("Key cannot be null or empty")
        if plainText == None or plainText == "":
            raise ValueError("Plaintext cannot be null or empty")


    def decrypt(self, ciphertext, key):
        if key == None or key == "":
            raise ValueError("Key cannot be null or empty")
        if ciphertext == None or ciphertext == "":
            raise ValueError("Ciphertext cannot be null or empty")
        print(ciphertext)
        print(key)

to_decrypt = AES256()
to_decrypt.decrypt(ciphertext = "ANJIE", key = "123")