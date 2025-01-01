from Crypto.Cipher import AES
from pwn import xor
import requests

# Fetch encrypted flag
def fetch_encrypted_flag():
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    response = requests.get(url)
    return response.json()['ciphertext']

# Decrypt a block using ECB mode
def decrypt_block(block):
    url = f"http://aes.cryptohack.org/ecbcbcwtf/decrypt/{block}/"
    response = requests.get(url)
    return response.json()['plaintext']

# Main decryption logic
def decrypt_flag():
    encrypted_flag = fetch_encrypted_flag()
    # Split into 32-byte (16-byte block in hex) chunks
    blocks = [encrypted_flag[i:i+32] for i in range(0, len(encrypted_flag), 32)]
    iv = blocks[0]  # Extract IV
    ciphertext_blocks = blocks[1:]  # Remaining blocks are ciphertext

    plaintext = []
    previous_block = iv

    for block in ciphertext_blocks:
        # Decrypt current block
        decrypted = decrypt_block(block)
        # XOR decrypted block with previous ciphertext block (or IV for the first block)
        plaintext_block = xor(bytes.fromhex(decrypted), bytes.fromhex(previous_block))
        plaintext.append(plaintext_block)
        # Update previous_block for next iteration
        previous_block = block

    # Combine plaintext blocks and decode
    flag = b"".join(plaintext).decode()
    print(f"Decrypted Flag: {flag}")

if __name__ == "__main__":
    decrypt_flag()
