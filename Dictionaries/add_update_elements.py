login = {"name": "George", "email" : "george@email.com", "login": "2025-04-15 11:40"}

print("The initial dictionary is \t ->", login)


# modify the name
login["name"] = "George Calin"
print("The dictionary after modification is \t ->", login)

# add a new element to the dictionary
login["mobile"] = "0722 764 836"
print("The dictionary after modification is \t ->", login)

# modify multiple elements at once (update and add new element)
login.update({"name":"Mara", "email": "some@email.ro", "new phone": "1111"})
print("The dictionary after modification is \t ->", login)