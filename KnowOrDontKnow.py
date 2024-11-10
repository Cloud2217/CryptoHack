data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert hex string to bytes
data_bytes = bytes.fromhex(data)

# Derive the partial key by XORing the beginning with "crypto{"
partial_key = bytes([a ^ b for a, b in zip(data_bytes[:7], b"crypto{")])

# Extend the key by repeating it to match the length of data_bytes
key = (partial_key + b'y') * (len(data_bytes) // len(partial_key + b'y')) + (partial_key + b'y')[:len(data_bytes) % len(partial_key + b'y')]

# Decrypt the flag by XORing each byte of data with the key
flag = bytes([a ^ b for a, b in zip(data_bytes, key)])

# Print the result
print("FLAG =", flag.decode("utf-8"))
