# we use class attributes to store attributes that are either common to all attributes or unrelated to any attribute
# we shall prefer using class attributes to avoid wasting memory of storing common object attributes in instance attributes


class Person:
    """
    this class describes a Person and appears in the __doc__ class attributes
    """
    location = "Romania" # this attribute is not specific to an individual object

    def __init__(self, name, age, job):
        self.name = name # this is an instance attribute
        self.age = age   # this is an instance attribute
        self.job = job   # this is an instance attribute

    def change_name(self,new_name):
        """
        describes the method
        :param new_name:
        :return:
        """
        pass


person = Person("George", 46, "Manager")
print(Person) # prints the class object # <class '__main__.Person'>
print(person) # prints the object constructed using the class model # <__main__.Person object at 0x0000016beb7ea650>

print(vars(Person)) # prints the class attributes and methods
# '__module__': '__main__', '__doc__': '\n    this class describes a Person and appears in the __doc__ class attributes\n    ', 'location': 'Romania', '__init__': <function Person.__init__ at 0x0000016beb7ef920>, 'change_name': <function Person.change_name at 0x0000016beb7ef9c0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}


print(vars(person)) # prints the instance attributes
# {'name': 'George', 'age': 46, 'job': 'Manager'}