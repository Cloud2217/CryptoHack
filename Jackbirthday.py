n = 1 << 11  # n = 2^11 = 2048
P = 1  # Initial probability
factor = 1 - 1/n  # Precompute the factor to avoid repeated calculations
for i in range(1, n):
    P *= factor  # Incrementally calculate P as (1 - 1/n)^i
    nP = 1 - P  # 1 minus the probability
    if nP > 0.5:
        print(i)
        break
