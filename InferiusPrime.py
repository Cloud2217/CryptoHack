from Crypto.Util.number import long_to_bytes

# RSA parameters
modulus = 742449129124467073921545687640895127535705902454369756401331
public_exponent = 3
ciphertext = 39207274348578481322317340648475596807303160111338236677373
prime1 = 752708788837165590355094155871
prime2 = 986369682585281993933185289261

# Compute the private exponent
totient = (prime1 - 1) * (prime2 - 1)
private_exponent = pow(public_exponent, -1, totient)

# Decrypt the ciphertext
plaintext = pow(ciphertext, private_exponent, modulus)

# Convert the plaintext to bytes and print
print(long_to_bytes(plaintext))
