from sympy import mod_inverse

# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Step 1: Calculate N
N = p * q

# Step 2: Calculate φ(N) = (p - 1) * (q - 1)
phi_N = (p - 1) * (q - 1)

# Step 3: Calculate the modular inverse of e mod φ(N) to get d
d = mod_inverse(e, phi_N)

# Output the result
print("The private key d is:")
