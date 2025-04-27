# in Python anything is an object, thus even a class is an object
# for instance an int value is an object of a int class, a string is an object of the string class
# for the class case, the class name is the reference variable to the class object , make the difference between the class object and the objects of the class

class Person:
    """
    this class describes a person and will appear in the __doc__ class attribute
    """
    pass

print(Person) # <class '__main__.Person'>
print(vars(Person)) # {'__module__': '__main__', '__doc__': '\n    this class describes a person and will appear in the __doc__ class attribute\n    ', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
