element = 3
modulo = 13

# Compute the modular inverse using Fermat's Little Theorem
print("FLAG =", pow(element, modulo - 2, modulo))
