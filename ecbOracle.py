import requests
import string

url = "http://aes.cryptohack.org/ecb_oracle/"

# Starting plaintexts
s0 = 'a' * 16
s1 = 'a' * 16
charset = string.printable  # Using printable characters for more options
flag = ''
t = ''

# Loop through the flag positions
for i in range(31):
    s1 = s1[1:] + t  # Update s1 with the current known flag part
    for j in charset:  # Try every printable character
        c = s0 + s1 + j + 'a' * (31 - i)  # Construct the payload
        c = c.encode().hex()  # Convert payload to hexadecimal
        r = requests.get(f"{url}/encrypt/{c}")  # Send request to encryption oracle
        data = r.json()  # Get JSON response
        cipher = data["ciphertext"]  # Extract ciphertext from the response
        cipher = bytes.fromhex(cipher)  # Convert ciphertext from hex to bytes

        # Check for matching blocks (ECB mode property)
        if cipher[16:32] == cipher[48:64]:
            flag += j  # Append the found character to the flag
            t = j  # Update the known part of the flag
            print(flag)  # Print the flag progress
            break  # Move to the next position once a match is found
