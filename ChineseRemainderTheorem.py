# Given values for modular congruences
mod1, mod2, mod3 = 5, 11, 17
N = mod1 * mod2 * mod3  # 935

# Calculate the individual terms
n1, n2, n3 = N // mod1, N // mod2, N // mod3  # 187, 85, 55

# Compute e1, e2, e3 to satisfy the modular inverse requirements
e1, e2, e3 = 561, 595, 715  # Precomputed values for simplification

# Compute x using the values
x = 2 * e1 + 3 * e2 + 5 * e3

# Output the final answer
print("FLAG =", x % N)
