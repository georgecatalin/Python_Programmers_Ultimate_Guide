# formatting numbers into strings
my_number = 34567890
print("{0:,}".format(my_number)) # 34,567,890 , although this does not account for the culture settings of formatting numbers en-us, uk etc
print("{0:+}".format(my_number)) # adds the + sign
print("{0:+.2f}".format(my_number)) # +34567890.00 adds two decimal points

my_number_1 = 0.45
print("{0:+%}".format(my_number_1)) # + 45.0000000%
print("{0:.2%}".format(my_number_1)) # 45.00

# mix variables in strings
# 'John lives in New York'

# option 1 concatenation of strings
name = "John"
city = "New York"
statement = " lives in "
print(name + statement + city)

# index order
print("{} lives in {}".format(name,city))

# positional order
print("{1} is a beautiful city and {0} lives in {1}".format(name,city))

# named order
print("{a} is a beatiful city and {b} lives in {a}.".format(b = name, a = city))

# f-string
print(f"{city} is a beautiful city and {name} lives in {city}.")