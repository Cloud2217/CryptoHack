# Given hex string
hex_string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

# Convert hex string to bytes
data = bytes.fromhex(hex_string)

# Try all possible single-byte XOR values (0-255)
for key in range(256):
    decrypted = bytes([b ^ key for b in data])
    
    # Check if the result is printable ASCII
    if all(32 <= c <= 126 for c in decrypted):
        message = decrypted.decode('utf-8', errors='ignore')
        print(f"Key: {key} => Message: {message}")

        # Stop if we find a clearly readable message
        if "crypto" in message:
            break
