def extended_gcd(a, b):
    """Return (gcd, x, y) such that a*x + b*y = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(g, p):
    """Find the multiplicative inverse of g modulo p using the Extended Euclidean Algorithm"""
    gcd, x, _ = extended_gcd(g, p)
    if gcd != 1:
        raise ValueError(f"No inverse exists for {g} modulo {p}")
    return x % p

# Given values
p = 991
g = 209

# Find the inverse
d = mod_inverse(g, p)
print(f"The multiplicative inverse of {g} modulo {p} is {d}")
