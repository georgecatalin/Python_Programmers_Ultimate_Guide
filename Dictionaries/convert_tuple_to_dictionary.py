a_tuple_containing_keys = ("name", "age","gender")

print("The initial tuple is \t ->", a_tuple_containing_keys)

# convert the tuple to dictionary placing the None as value for each key
dictionary_from_tuple_ver_1 = dict.fromkeys(a_tuple_containing_keys)
print("Here is the dictionary converted from the tuple \t ->", dictionary_from_tuple_ver_1)

# convert the tuple to dictionary placing a default value for each key (specify the value in the constructor of the dictionary)
dictionary_from_tuple_ver_2 =dict.fromkeys(a_tuple_containing_keys,"standard value")
print("Here is the dictionary converted from the tuple \t ->", dictionary_from_tuple_ver_2)

# convert from a list containing tuples which hold, each of them , both key , value pairs into a single record dictionary
list_of_tuples_to_be_converted = [("name", "George"),("age",46),("dog","Zizou")]
my_dictionary = dict(list_of_tuples_to_be_converted)
print("Here is the dictionary converted from the tuple \t ->",my_dictionary )