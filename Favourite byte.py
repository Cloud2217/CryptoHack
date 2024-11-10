# Given hex string
hex_string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

# Convert hex string to bytes
data = bytes.fromhex(hex_string)

# Try all possible single-byte XOR values (0-255) and print decrypted messages
for key in range(256):
    decrypted_message = ''.join(chr(b ^ key) for b in data)
    print(f"Key: {key} => Decrypted Message: {decrypted_message}")
