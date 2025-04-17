this_set = {"Maths", "Physics", "Chemistry"}

print("The set is \t ->", this_set)

# loop in a set iterable
for i in this_set:
    print("Element of the set is :", i)

# loop through index using range() can not be utilized because set collections are unordered and unindexable

# loop with enumerate() function can be used , but the tuples change from one run to other as sets are not ordered
for i in enumerate(this_set):
    print(i,i[0],i[1])