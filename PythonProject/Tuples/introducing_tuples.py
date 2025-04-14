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