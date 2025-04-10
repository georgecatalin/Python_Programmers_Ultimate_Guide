my_string = "someone@sample.com"

# this is a reminder about how to check strings without the use of regular expressions

# 'in' and 'not in'
print("someone" in my_string) # True
print("email" in my_string) # False
print("someone" not in my_string) # False
print("email" not in my_string) # True

# methods: 'startswith()' and 'endswith'
print(my_string.startswith("some")) # True
print(my_string.startswith("email")) # False
print(my_string.endswith(".com")) # True
print(my_string.endswith("email")) # False

# methods: 'count()'
print(my_string.count("o")) # 3

# methods: 'index()' and 'find()'
print(my_string.index("o")) # 1
print(my_string.index("o"),2) # starts counting from the previous position where found + 1
# print(my_string.index("z")) # 'substring not found' error

print(my_string.find("o")) # 1
print(my_string.find("o",2)) # starts counting from the previous position where found + 1
print(my_string.find("z")) # returns -1 in case if not found ; aside of this find() is similar to index()

# methods: 'rindex()' and 'rfind()' -> rearindex() and readfind() similar like the previous
print(my_string.rindex("o")) # 16

# functions: 'len()
print(len(my_string)) # 18