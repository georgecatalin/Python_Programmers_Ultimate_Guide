this_tuple = (14,6.4,"Mara",47,6.4,"Hello",6.4)

# one can search in tuples using the methods .count() , index() and in, not in operators

print(this_tuple.count(6.4)) # 3
print(this_tuple.index(6.4)) # 1 which is the first occurrence
print(this_tuple.index(6.4,2)) # 4 which is the next occurrence, starting to check from index 2
# print(this_tuple.index(12)) # value not found error

print(14 in this_tuple) # True
print(1978 in this_tuple) # False

print(6.4 not in this_tuple) # False
print(1954 not in this_tuple) # True
