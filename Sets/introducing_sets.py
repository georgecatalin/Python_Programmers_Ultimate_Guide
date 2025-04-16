# sets are another type of collections: unordered, (thus) unindexable, mutable, not duplicable
# sets arose from the need to store only unique values

city_set = {"Galati","Focsani","Tulcea","Braila","Galati"} # even if the same element is added by mistake duplicate, it will not be stored

print("The set is \t ->", city_set) # {'Braila', 'Galati', 'Focsani', 'Tulcea'} # with every new display on the screen , the order of elements is different
print(type(city_set)) # <class 'set'>
print(len(city_set)) # number of elements in the set -> 4

# how to create a new set
print(type({})) # <class 'dict'>
print(type(set())) # <class 'set'>

# sets can only store immutable types which are hashable types: int, float, complex, str, bool, tuple, range, frozen set
# sets can not store mutable types because these are not hashable : lists, dictionaries and other sets

# add an element to the set

city_set.add("Bucharest")
print("The  new set is \t ->", city_set) # {'Braila', 'Galati', 'Focsani', 'Tulcea'}