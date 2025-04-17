my_list = [ 78.56, 879.45, 3245.53, 1204.56, 567.56, 898.56]

"""
* all() and any() functions return a boolean value of True or False
* all() returns True if all separate elements are True
* any() returns True if , at least one element is True
"""

print([(price >=1000) for price in my_list]) # [False, False, True, True, False, False]

print(all([(price >= 1000) for price in my_list ])) # False
print(any([(price >= 1000) for price in my_list])) # True cause at least one is True

