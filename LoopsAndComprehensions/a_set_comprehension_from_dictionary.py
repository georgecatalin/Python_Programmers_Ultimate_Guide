this_list_of_dictionaries = [
    {"name":"George", "score":9.5},
    {"name":"Mara", "score": 9.8},
    {"name":"George", "score":7.5},
    {"name":"Mara", "score":6.8}
]

# create a set containing the unique names for the list of dictionaries

print(set(item["name"] for item in this_list_of_dictionaries))

# or

print({item["name"] for item in this_list_of_dictionaries})