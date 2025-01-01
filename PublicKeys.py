# Define the message and RSA parameters
message = 12
e = 65537
p = 17
q = 23

# Calculate the modulus N = p * q
N = p * q

# Encrypt the message using modular exponentiation
ciphertext = pow(message, e, N)

# Output the ciphertext
print("The ciphertext is:", ciphertext)
