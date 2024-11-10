def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Given hex strings
KEY1_hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_xor_KEY1_hex = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2_xor_KEY3_hex = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAG_xor_keys_hex = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

# Step 1: Convert hex strings to bytes
KEY1 = bytes.fromhex(KEY1_hex)
KEY2 = xor_bytes(bytes.fromhex(KEY2_xor_KEY1_hex), KEY1)
KEY3 = xor_bytes(bytes.fromhex(KEY2_xor_KEY3_hex), KEY2)

# Step 2: Calculate FLAG
FLAG = xor_bytes(xor_bytes(xor_bytes(bytes.fromhex(FLAG_xor_keys_hex), KEY1), KEY2), KEY3)

# Output the flag
print(f"FLAG (hex): {FLAG.hex()}")
print(f"FLAG (decoded): crypto{{{FLAG.decode('utf-8', errors='ignore')}}}")
