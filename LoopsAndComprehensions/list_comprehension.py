"""
* comprehensions can be applied to all kinds of collections in Python like lists, tuples, sets, dictionaries, frozen sets
* the syntax of a comprehension is:  [expression for variable in collection if condition]
* the comprehensions create new collections , and they do not modify the collections they are applied to
"""

my_list = [ 78.56, 879.45, 3245.53, 1204.56, 567.56, 898.56]

# a list comprehension without expression and without filter
print([0 for var in my_list])

# a list comprehension with expression and without filter
print(["hello" for item in my_list])

# a list comprehension with expression and without filter
print([(item_1 + 1) for item_1 in my_list])

# a list comprehension with expression and without filter
print([round(item * 0.8) for item in my_list] )

# a list comprehension with expression and with filter
print([round(price * 2) for price in my_list if price >= 800])