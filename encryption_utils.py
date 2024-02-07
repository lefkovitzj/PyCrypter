"""
    Author: AaronTook (https://AaronTook.github.io)
    Version: 1.0.0
    Version Launch Date: 2/6/2024
    File Last Modified: 2/6/2024
    Project Name: PyCrypter
    File Name: encryption_utils.py
"""

# Third-party Module Imports
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def encrypt_file(file_location, pass_phrase):
    """ Encrypt a file using the given password. """
    try:
        salt = get_random_bytes(32)
        key_bytes = PBKDF2(pass_phrase, salt, dkLen=32) # Your key that you can encrypt with
        encryption_cipher = AES.new(key_bytes, AES.MODE_EAX)
        nonce = encryption_cipher.nonce
        data = open(file_location, "rb").read()
        ciphertext, tag = encryption_cipher.encrypt_and_digest(data)
        
        with open(file_location+".bin", "wb") as output_file:
            output_file.write(salt)
            output_file.write(nonce)
            output_file.write(tag)
            output_file.write(ciphertext)
        
        return True, "File encrypted successfully"
    except FileNotFoundError:
        return False, "File does not exist"
    except:
        return False, "Something went wrong in the encryption process"

def decrypt_file(file_location, pass_phrase):
    """ Decrypt a previously-encrypted file using the given password. """
    try:
        with open(file_location, "rb") as input_file:
            salt = input_file.read(32)
            encryption_nonce = input_file.read(16)
            encryption_tag = input_file.read(16)
            ciphertext = input_file.read()
        key_bytes = PBKDF2(pass_phrase, salt, dkLen=32) # The key that was used for encryption.
        decryption_cipher = AES.new(key_bytes, AES.MODE_EAX, encryption_nonce)
        data = decryption_cipher.decrypt_and_verify(ciphertext, encryption_tag)
        
        with open(file_location[:-4], "wb") as output_file:
            output_file.write(data)
        
        return True, "File decrypted successfully"
    except FileNotFoundError:
        return False, "File does not exist"
    except:
        return False, "Something went wrong in the decryption process"