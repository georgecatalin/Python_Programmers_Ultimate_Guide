person_dictionary_1 = {"name": "Mara Calin", "email": "email@address.ro", "phone": "1234-556"}

print("The initial dictionary 'person_dictionary_1' is \t ->", person_dictionary_1)


# person_dictionary_1 is a variable on the stack storing the memory address of the dictionary object on the arena, inside the object pool

person_dictionary_2 = person_dictionary_1 # the memory address of the dictionary object in the object pool is passed to the new variables

# hence both are referencing the same object in the object pool of the arena
person_dictionary_1["name"] = "George Calin"
print("The initial dictionary 'person_dictionary_1' is \t ->", person_dictionary_1)
print("The initial dictionary  'person_dictionary_2' is \t ->", person_dictionary_2) # modification is visible in both cause they are pointing to the same object


# there is another way of copying by creating a whole new copy of the initial object
person_dictionary_3 = person_dictionary_1.copy()
person_dictionary_1["name"] = "Sorina"
print("The initial dictionary 'person_dictionary_1' is \t ->", person_dictionary_1)
print("The initial dictionary 'person_dictionary_3' is \t ->", person_dictionary_3) # this time the objects are decoupled

person_dictionary_4 = dict(person_dictionary_1)
person_dictionary_1["name"] = "Zizou"
print("The initial dictionary 'person_dictionary_1' is \t ->", person_dictionary_1)
print("The initial dictionary 'person_dictionary_4' is \t ->", person_dictionary_4) # this time the objects are decoupled

person_dictionary_5 = {**person_dictionary_1} # **  is the kwargs operator ** from key, value pair
person_dictionary_1["name"] = "Milla"
print("The initial dictionary 'person_dictionary_1' is \t ->", person_dictionary_1)
print("The initial dictionary 'person_dictionary_5' is \t ->", person_dictionary_5) # this time the objects are decoupled
