from Crypto.Cipher import AES
import base64

def encrypt(data,key):
    """It encrypts given data with using AES-256"""
    cipher = AES.new(key, AES.MODE_EAX) # AES generates encryption object in EAX mode
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8')) # Encrypts data
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8') # It encodes with base64 and returns

def decrypt(data,key):
    """It decrypts data with using AES-256"""
    raw = base64.b64decode(data)
    nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:] # It seperates AES blocks
    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce) # It generates AES decryption object
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8') # It decrypts data and returns