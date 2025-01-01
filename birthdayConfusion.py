from math import factorial

n = 2048
factorial_n = factorial(n)  # Precompute factorial(n) once
for i in range(n):
    # Efficient calculation of probability
    numerator = factorial_n
    denominator = factorial(n - i) * pow(n, i)
    probability = 1 - (numerator / denominator)
    
    if probability > 0.75:
        print(i)
        break
