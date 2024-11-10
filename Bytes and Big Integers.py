from Crypto.Util.number import long_to_bytes

# Convert integer to bytes and decode as UTF-8 string in one line
print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269).decode('utf-8'))
