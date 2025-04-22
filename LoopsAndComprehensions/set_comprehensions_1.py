this_set = {1024.5, 923.3, 1024.5, 567.64, 897.45, 923.3}

print(this_set) # {1024.5, 897.45, 923.3, 567.64} # only the unique values

"""
syntax:
    expression for variable in collection if condition
"""

print({element for element in this_set})
print(set(element for element in this_set))
print(frozenset(element for element in this_set)) # this is immutable