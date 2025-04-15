user = { "email": "user@email.ro", "phone": "1234-45454", "age":46, "gender": "Male"}

print("The initial dictionary is \t ->", user)

# one can remove elements with .pop(), .popitem(), .clear(), del

removed_value = user.pop("email")
print("The value being removed is \t ->", removed_value)
print("The modified dictionary \t ->", user)

# user.pop("job") # KeyError: 'job' does not exist
#print("The modified dictionary \t ->", user)

removed_value_1 = user.popitem() # removes last key,value pair element
print("The value being removed is \t ->", removed_value_1)
print("The modified dictionary \t ->", user)

# remove with del function
del user["phone"]
print("The modified dictionary \t ->", user)

# clear all the elements of the dictionary
user.clear()
print("The modified dictionary \t ->", user)

# delete the dictionary object itself
del user