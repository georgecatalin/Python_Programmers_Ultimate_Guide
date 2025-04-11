# In Python, the memory is allocated dynamically into two sections:
# 1. stack
# 2. arena : contains one or more object pools (all objects, including literal values are objects in Python)
# Variables in Python are stored in the stack and they contain the addresses to the objects (like reference variables in C# or pointers in C)

print("id(1978) \t ->" , id(1978)) # memory is allocated
print("id(1978) \t ->", id(1978), " because this object was already created in the pool , it is being reused ") # because this object was already created in the pool , it is being reused
print("id(1978) \t ->", id(1978)) # because this object was already created in the pool , it is being reused
print("id(1978) \t ->", id(1978)) # because this object was already created in the pool , it is being reused

print(" " * 20)

print("Mara \t ->" , id("Mara")) # memory address is allocated
print("Mara \t ->", id("Mara")) # because this object was already created in the pool , it is being reused
print("Mara \t ->", id("Mara")) # because this object was already created in the pool , it is being reused
print("Mara \t ->", id("Mara")) # because this object was already created in the pool , it is being reused

print(" " * 20)

number = 1978
print("number = 1978")
print("id(number) \t ->" , id(number), " because this object was already created in the pool , it is being reused ")
print("id(number) \t ->" , id(number), " because this object was already created in the pool , it is being reused ")
print("id(number) \t ->" , id(number), " because this object was already created in the pool , it is being reused ")


new_number = number
print("id(new_number) =",id(new_number), "\t id(number) =", id(number))  # when copying, the address of the object in the object pool is copied in the new variables, hence now both variables point to the same value object
print("new_number=",new_number, "\tnumber=", number)

other_number = 1978
print("memory address of other_number = ", id(other_number)) # it found the object in the object pool and it stores its address

number = 1954 # 'number' variable stores the address of the new object '1954' and the other variables store the old memory addresses
print("new_number=",new_number, "\tnumber=", number)
print("id(new_number) =",id(new_number), "\t id(number) =", id(number))

# in Python ints and strings are immutable types

# the objects from the object pool that lose references from the stack are automatically deleted by the garbage collector
# the objects can be deleted manually by the developer on condition that there is no ohter variable poiting to it
del number
#  print(id(number))  # -> NameError: name 'number' is not defined