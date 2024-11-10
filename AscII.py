# Convert ASCII values to characters and join them into a single string
flag = ''.join(chr(value) for value in [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125])

# Print the resulting flag
print(flag)
