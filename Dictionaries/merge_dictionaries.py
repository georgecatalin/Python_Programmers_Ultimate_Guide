user_dictionary = {"name":"George Calin", "job":"IT Project Manager"}
user_details_dictionary = {"location":"Galati", "country":"Romania"}

# there are 3 possibilities to perform a merge of dictionaries with Python

# manner 1
user_complete_dictionary = user_dictionary.copy() # create a copy of the initial dictionary
user_complete_dictionary.update(user_details_dictionary) # update the new dictionary adding what is

print("The merged dictionary is \t ->", user_complete_dictionary )

# manner 2 with kwargs (**)
user_complete_dictionary_kwargs = {**user_dictionary,**user_details_dictionary}
print("The merged dictionary is \t ->", user_complete_dictionary_kwargs)

# manner 3 with the union operator | (As of Python 3.9)
user_complete_dictionary_union_operator = user_dictionary | user_details_dictionary
print("The merged dictionary is \t ->", user_complete_dictionary_union_operator)

# in case if both dictionaries contain the same key, then the lastly executed operation on dictionary matters and gives the value of the key which is common
user_dictionary_common_key = {"name":"George Calin", "job":"IT Project Manager"}
user_details_dictionary_common_key = {"location":"Galati", "country":"Romania", "job":"Developer"}

user_complete_details_common_key = user_dictionary_common_key.copy()
user_complete_details_common_key.update(user_details_dictionary_common_key)
print("The merged dictionary is \t ->", user_complete_details_common_key) # user_details_dictionary_common_key is the last processed and the key is taken from there