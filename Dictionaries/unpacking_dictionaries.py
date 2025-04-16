my_dictionary = {"name":"George","age":46, "gender":"Male", "email":"george.calin@gmail.com", "dog":"Zizou"}

print(f"The dictionary is \t -> {my_dictionary}")

# unpacking into keys variables (standard)
var1, var2, var3, var4, var5 = my_dictionary
print(f"The keys variables after unpacking \t -> {var1}, {var2}, {var3} and {var4}")

# unpacking into value variables
value1, value2, value3, value4,value5 = my_dictionary.values()
print(f"The keys variables after unpacking \t -> {value1}, {value2}, {value3} and {value4}")

# unpacking into value variables partly with the splat *  operator
value01, value02, *others = my_dictionary.values() # others object will hold a list with the remaining values
print(f"The keys variables after unpacking \t -> {value01}, {value02}, {others}")
