import hashlib
import codecs
from Crypto.Cipher import AES

# Load the dictionary
def load_words(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

# Decrypt function
def decrypt_flag(ciphertext, key_hash):
    try:
        cipher = AES.new(bytes.fromhex(key_hash), AES.MODE_ECB)
        decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
        return decrypted.hex()
    except (ValueError, KeyError):
        return None

# Brute-force function
def brute_force_decrypt(flag, word_list):
    for word in word_list:
        key_hash = hashlib.md5(word.encode()).hexdigest()
        decrypted_hex = decrypt_flag(flag, key_hash)
        if decrypted_hex:
            try:
                decrypted_text = codecs.decode(decrypted_hex, 'hex').decode('ascii')
                print(f"Flag found: {decrypted_text}")
                return
            except (UnicodeDecodeError, ValueError):
                continue
    print("No valid flag found.")

# Main execution
if __name__ == "__main__":
    WORD_FILE = "words"
    ENCRYPTED_FLAG = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    
    words = load_words(WORD_FILE)
    brute_force_decrypt(ENCRYPTED_FLAG, words)
