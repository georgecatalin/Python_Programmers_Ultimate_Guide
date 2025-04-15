# Tuples are collection classes with the following features:
#   * ordered, indexable, immutable(unlike lists which are mutable), duplicatable
# we generally use Lists to store elements of the same data type, practically all the elements of the same column in a database
# we generally use tuples to store records of data which contain multiple fields of different data types

# id , name, surname, email, gender, IP address, duplicate_name
record_one_tuple = (1,"Ward","Cheatle",	"wcheatle0@blogger.com", "Male","250.142.176.128", "Ward" ) # one can use the parentheses () or not , it is not compulsory for tuples, although it makes them more readable

print("The tuple is  -> \t", record_one_tuple)
# indexable
print(record_one_tuple[1]) # "Ward"

# as the tuple is immutable , one can not modify elements of the tuple, one can not add new elements to the tuple, and one can not remove elements of the tuple
# record_one_tuple[2] = "Something"

# how to create an empty typle
this_tuple = ()
this_tuple_1 = tuple()

print(type(this_tuple))
print(type(this_tuple_1))

# how to create a tuple hosting a single element
single_element_tuple = ("George") # note that the parenthesis around the string, does not make it a tuple,they can be ommitted
print(type(single_element_tuple)) # <class 'str'>

single_element_tuple_real = ("George",)
print(type(single_element_tuple_real)) # <class 'tuple'>

single_element_tuple_constructor = tuple("Mara")
print(single_element_tuple_constructor)
print(type(single_element_tuple_constructor))