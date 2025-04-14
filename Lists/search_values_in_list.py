mixed_list = [
    "Zizou",               # Dog's name (string)
    "Zizou",               # Duplicate string
    42,                    # The answer to life, the universe, and everything (int)
    3.14,                  # Pi (float)
    True,                 # Boolean value
    False,                # Boolean value
    [1, 2, 3],             # A simple list (nested)
    {"name": "Mara"},      # Dictionary (child's name)
    {"name": "Mara"},      # Duplicate dictionary
    42,                    # Duplicate integer
    "coffee",              # Because devs survive on it
    None,                  # Represents absence of value
    "coffee",              # Duplicate string
    3.14,                   # Duplicate float
    46

]

# in
print(3.14 in mixed_list) # True (multiple occurrences)
print(46 in mixed_list) # True (single occurrence)
print(1000 in mixed_list) # False

# not in
print(1000 not in mixed_list) # True
print("Zizou" not in mixed_list) # False

# count occurrences
print(mixed_list.count("Zizou")) # 2
print(mixed_list.count("Milla")) # 0

# index of element
print(mixed_list.index("Zizou")) # 0
print(mixed_list.index("Zizou", 1)) # 1
# print(mixed_list.index("George")) # Value not found error , before checking for index, make sure the object exists in the list
# ValueError: 'George' is not in list