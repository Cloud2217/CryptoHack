import sympy

# The 150-bit number to be factorized
N = 510143758735509025530880200653196460532653147

# Attempt factorization
factors = sympy.ntheory.factorint(N)

# Extract the smaller prime factor
smaller_prime = min(factors.keys())
print("The smaller prime factor is:", smaller_prime)
