# In Python there are :
# 1. immutable types: int, float, complex, str, bool + tuple, range, frozenset
# 2. mutable types: list, set, dictionary, others
# the difference between the two lies in the manner they can change or not


string_1 = "Hello"
print("id(old) \t ->", id(string_1), " its value = \t ->", string_1)

string_1 = string_1 + "World" # a new object is created in the arena (256kb by default) with the value "Hello World" and string_1 points to the new object
print("id(new) \t ->" ,id(string_1)," its value = \t ->", string_1)