from sympy.ntheory import is_primitive_root

def find_smallest_primitive(p):
    g = 2
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

# Given prime p
p = 28151

# Find and print the smallest primitive element
smallest_g = find_smallest_primitive(p)
print("The smallest primitive element is:", smallest_g)
