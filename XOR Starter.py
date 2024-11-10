# XOR each character in "label" with the integer 13 and format the result
print(f"crypto{{{''.join(chr(ord(char) ^ 13) for char in 'label')}}}")
