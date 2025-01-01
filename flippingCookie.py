import requests
from Crypto.Util.number import *
url = "http://aes.cryptohack.org/flipping_cookie/"

# Make the initial request to get the cookie
response = requests.get(f"{url}get_cookie")
data = response.json()
cookie = data["cookie"]

# Extract IV and ciphertext from the cookie
iv = bytes.fromhex(cookie[:32])
ciphertext = bytes.fromhex(cookie[32:])

# Modify the IV to flip the required bits to convert 'admin=False' to 'admin=True'
iv_modified = iv[:6] + bytes([iv[6]^ord('F')^ord('T')]) + bytes([iv[7]^ord('a')^ord('r')]) + bytes([iv[8]^ord('l')^ord('u')]) + bytes([iv[9]^ord('s')^ord('e')]) + bytes([iv[10]^ord('e')^ord(';')]) + iv[11:]

# Convert the modified IV and ciphertext to hex
iv_modified_hex = iv_modified.hex()
ciphertext_hex = ciphertext.hex()

# Check if the server grants admin access with the flipped bits
check_url = "http://aes.cryptohack.org/flipping_cookie/check_admin"
response = requests.get(f"{check_url}/{ciphertext_hex}/{iv_modified_hex}")

# Print the response from the server
response_data = response.json()
print(response_data)


