# dictionaries {} address the mishaps from tupes: immutability and the lack of keys
# dictionaries are:
#   ordered (from Python 3.7 onwards)
#   not indexable
#   key/value paired (keys can be ints, floats, strings and tuples whilst values can hold any data type)
#   are not duplicatable cause the key, value pair is unique


friends_dictionary = {"name": "George", "email": "george.calin@gmail.com", "phone" : "0722 764 836"}

print("The dictionary \t ->", friends_dictionary)
print("Type \t ->", type(friends_dictionary)) # <class 'dict'>
print("Number of elements in the dictionary \t ->", len(friends_dictionary)) # 3

# how to read an element of the dictionary sequence (collection type)
print("The name is \t ->", friends_dictionary["name"])
# print("The surname is \t ->", friends_dictionary["surname"]) # KeyError: 'surname' because it does not exists

# read the elements of the dictionary with the .get() method
print("The name is \t ->", friends_dictionary.get("name"))
print("The surname is \t ->", friends_dictionary.get("surname")) # unlike before , when trying to access by key, no error returned but "None"

# there is an overload of the .get() method to specify what to return in case of "None"
print("The surname is \t ->", friends_dictionary.get("surname", "unknown surname")) # unknown surname

