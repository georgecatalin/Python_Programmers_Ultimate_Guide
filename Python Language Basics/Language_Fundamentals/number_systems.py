
number_1 = 1978
binary_converted_number_1 = bin(number_1)
print("Binary converted number {} \t is \t {}".format(number_1,binary_converted_number_1))

octal_converted_number_1 = oct(number_1)
print("Octal converted number {} \t is \t {}".format(number_1,octal_converted_number_1))

hexa_converted_number_1 = hex(number_1)
print("Hexa converted number {} \t is \t {}".format(number_1,hexa_converted_number_1))

# convert from binary, octal and hexa numbers to decimal numbers
print("convert from binary to decimal numbers ->", int(0b11110111010))
print("convert from octal to decimal numbers ->", int(0o3672))
print("convert from hexa  to decimal numbers ->", int(0x7ba))

# convert from binary to octal or hexa and viceversa
print("binary to octal ->", oct(0b11110111010)) # binary to octal
print("octal to binary ->", bin(0o3672)) # octal to binary
print("binary to hexa ->", hex(0b11110111010))

# convert from string containing binary, octal or hexa to decimal
print("convert from string containing binary to decimal -> ", int("0b11110111010", base=2))
print("convert from string containing octal to decimal -> ", int("0o3672", base=8))
print("convert from string containing hexa to decimal -> ", int("0x7ba", base=16))

# merge numbers into strings
print("merge binary numbers into strings -> {0:b}".format(number_1))
print("merge octal numbers into strings -> {0:o} ".format(number_1))
print("merge hexa numbers into strings -> {0:x} ".format(number_1))
