my_dictionary = {"name":"George Calin","age":46,"gender":"Male"}

list_keys = my_dictionary.keys()
list_values = my_dictionary.values()
list_tuples_key_value_pair = list(my_dictionary.items()) # my_dictionary.items() returns  a special object dict_values()

print(f"From the dictionary {my_dictionary} I get {list_keys} and {list_values} and {list_tuples_key_value_pair}")

# get elements from the tuple
print(list_tuples_key_value_pair[1]) # ('age', 46)
print(list_tuples_key_value_pair[1][1]) # 46