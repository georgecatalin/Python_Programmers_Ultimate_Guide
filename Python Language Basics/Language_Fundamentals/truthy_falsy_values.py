# in Python one can validate user's input data, by converting into bool()

my_string = ""
my_int = 0

print("Boolean converted ",bool(my_string)) # False
print("Boolean converted ",bool(my_int)) # False

# to validate all at once
print("validate both user inputs ->", bool(my_string) and bool(my_int)) # False

my_filled_string_1 = " "
print("Boolean converted ",bool(my_filled_string_1)) # True
my_filled_string_2 = " "
print("Boolean converted ",bool(my_filled_string_2)) # True

my_float =0.0
print("Boolean converted ",bool(my_float)) # False

my_complex = 0j
print("Boolean converted ",bool(my_complex)) # False

empty_list = []
print("Boolean converted ",bool(empty_list)) # False

empty_set = set()
print("Boolean converted ",bool(empty_set)) # False

empty_tuple = ()
print("Boolean converted ",bool(empty_tuple)) # False