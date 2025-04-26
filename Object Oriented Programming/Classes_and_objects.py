# object oriented programming is a better programming paradigm for code reusability
# classes are models to create the objects
# objects have properties associated (attributes) and behaviours/methods (operations they can perform)

class Employee: # we use Pascal case (Title case) for naming classes
    print("Hello from class") # classes are executed by Python at the moment of their definition, not when creating the object

object_1 = Employee()
print("Object1 = ", object_1) # objects are created on the heap (arena) which is the RAM memory, whereas reference variables like object_1 are created on the stack and they contain the memory address of the object they point to

object_2 = Employee()#
print("Object2 = ", object_2)
