list_of_dictionaries = [
    {"id":1, "name": "George", "age": 46},
    {"id":1, "name": "George", "age": 46},
    {"id":2, "name": "Mara", "age": 14},
    {"id":1, "name" :"George", "age": 46},
    {"id":2, "name": "Mara", "age": 14}
]

print([{item["id"]:item} for item in list_of_dictionaries])
# [{1: {'id': 1, 'name': 'George', 'age': 46}}, {1: {'id': 1, 'name': 'George', 'age': 46}}, {2: {'id': 2, 'name': 'Mara', 'age': 14}}, {1: {'id': 1, 'name': 'George', 'age': 46}}, {2: {'id': 2, 'name': 'Mara', 'age': 14}}]

# we extract to a dictionary because unlike lists, dictionaries do not allow duplicates
print({item["id"]:item for item in list_of_dictionaries})
# {1: {'id': 1, 'name': 'George', 'age': 46}, 2: {'id': 2, 'name': 'Mara', 'age': 14}}

print(list({item["id"]:item for item in list_of_dictionaries}))
# [1.2]

print(list({item["id"]:item for item in list_of_dictionaries}.values()))
#[{'id': 1, 'name': 'George', 'age': 46}, {'id': 2, 'name': 'Mara', 'age': 14}]