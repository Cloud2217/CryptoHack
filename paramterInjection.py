from pwn import *
from json import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

HOST = 'socket.cryptohack.org' 
PORT = 13371

def check_pkcs7_padding(data):
    padding_length = data[-1]
    padding = data[-padding_length:]
    return all(byte == padding_length for byte in padding)

def get_decrypted_flag(secret: int, iv_hex: str, encrypted_flag_hex: str):
    # Generate AES key from secret
    sha1 = hashlib.sha1()
    sha1.update(str(secret).encode('ascii'))
    aes_key = sha1.digest()[:16]
    
    # Convert hex to bytes
    iv = bytes.fromhex(iv_hex)
    encrypted_flag = bytes.fromhex(encrypted_flag_hex)
    
    # Initialize AES cipher
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(encrypted_flag)

    # Check for padding and return plaintext
    if check_pkcs7_padding(decrypted_message):
        return unpad(decrypted_message, 16).decode('ascii')
    return decrypted_message.decode('ascii')

def transmit_message(msg):
    return r.sendline(dumps(msg))

# Create remote connection
r = remote(HOST, PORT)

# Receive and parse data from Alice
r.recvuntil(b'Intercepted from Alice: ')
alice_data = loads(r.recvuntil(b'}'))

# Send data to Bob
r.recvuntil(b'Send to Bob: ')
transmit_message(alice_data)

# Send data to Alice with a new value
r.recvuntil(b'Send to Alice: ')
transmit_message({'B': hex(1)})

# Receive data from Alice
r.recvuntil(b'Intercepted from Alice: ')
alice_data = loads(r.recvuntil(b'}'))

iv = alice_data['iv']
encrypted_flag = alice_data['encrypted_flag']
shared_secret = 1

# Decrypt and print the flag
print(get_decrypted_flag(shared_secret, iv, encrypted_flag))
