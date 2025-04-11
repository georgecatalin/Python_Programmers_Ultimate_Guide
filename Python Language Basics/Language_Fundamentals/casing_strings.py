
my_string = "I love programming in Python 3."

upp = my_string.upper() # in Python strings are immutable, a new string in uppercase is created my_string remains the same
low = my_string.lower()
title  = my_string.title()
capitalize = my_string.capitalize()
swapcase = my_string.swapcase()


print(upp)
print(low)
print(title)
print(capitalize)
print(swapcase)

my_string_1 = "george1978"
print(my_string_1.isalnum()) # True because contains only alphabet characters and digits
print(my_string_1.isalpha()) # False, contains also digits
print(my_string_1.isdigit()) # False, contains also alphabet characters

print(low.islower()) # True
print(upp.isupper()) # True

my_space= " "
print(my_space.isspace()) # True