from convert_tuple_to_dictionary import my_dictionary

my_keys_list = ["name","gender","age"]
my_values_list =["George","male",46]

the_mapping_object = zip(my_keys_list,my_values_list) # this is an object that maps the keys to the values in the memory pool

my_dictionary = dict(the_mapping_object)
print(f"The dictionary from the conversion of the two lists {my_keys_list} and {my_values_list} is \t -> {my_dictionary}")
