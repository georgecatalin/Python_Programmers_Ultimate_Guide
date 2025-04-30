# custom exceptions are application specific exceptions (such as validation exceptions)
# custom exception inherit from the Exception super class



class Person:
    """
    This is a model for Person
    """

    #getter property for __age private attribute
    @property
    def age(self):
        return self.__age

    #setter property for __age private attribute
    @age.setter
    def age(self,value):
        if 16 <= value <= 75:
            self.__age = value
        else:
            raise InvalidAgeException(value, "The age must be between 16 and 75")

class InvalidAgeException(Exception): # all custom exception inherit from the super class Exception
    def __init__(self, age, message):
        self.age = age
        self.message = message

try:
    person_object = Person()
    person_object.age = 17 # setter ok
    print(person_object.age) # getter

    person_object.age = 80 # setter with InvalidAgeException
    print(person_object.age)
except InvalidAgeException as invalid_age_exception_object:
    print("ERROR: \nyou provided the age as {} and \nit should have adhered to the following rule: \t -> {}".format(invalid_age_exception_object.age,invalid_age_exception_object.message))