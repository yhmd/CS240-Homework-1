# Test boundary 
zero_binary = "00000000"
zero_decimal = int(zero_binary, 2)

print("Zero:")
print("Binary:", zero_binary)
print("Decimal:", zero_decimal)
print("")

largest_binary = "11111111"
largest_decimal = int(largest_binary, 2)

print("Largest 8-bit unsigned value:")
print("Binary:", largest_binary)
print("Decimal:", largest_decimal)
print("")

negative_binary = "11111111"
negative_decimal = int(negative_binary, 2)

if negative_binary[0] == "1":
    negative_decimal = negative_decimal - 2 ** len(negative_binary)

print("Negative two's-complement value:")
print("Binary:", negative_binary)
print("Decimal:", negative_decimal)