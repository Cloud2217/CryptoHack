# Step 1: Define the constants from the simplified equations
a = 836 * 3 - 335 * 2

# Step 2: Find the three-digit prime p that divides 'a' and is greater than the largest number in the sequence (851)
p = None
for possible_p in range(851, 1000):
    if a % possible_p == 0:
        p = possible_p
        break

# Step 3: Once we have p, we can use it to find x from the equation 4 * x ≡ 836 (mod p)
if p:
    x = 0
    while True:
        x += 1
        if (4 * x - 836) % p == 0:
            break

    # Print the result in the flag format
    print(f"FLAG = crypto{{{p},{x}}}")
else:
    print("Suitable prime p not found.")
