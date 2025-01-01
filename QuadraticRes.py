p = 29
ints = [14, 6, 11]

# Find and print the minimum value of a for which (a ** 2) % p is in ints
print("FLAG =", min(a for a in range(1, p) if (a ** 2) % p in ints))
