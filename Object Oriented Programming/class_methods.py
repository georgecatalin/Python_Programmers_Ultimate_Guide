# in Python , like in other programming languages there exist methods to handle class attributes, and not interact with specific objects
# a practical use of class methods could be to create an object based on a certain condition

from datetime import  date

class Person:
    """
    this is the class
    """
    location = "Galati"

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    @classmethod # this decorator has to be added to mark the method is a class method
    def create_object_from_date_of_birth(cls, name: str, birth_year: int, job:str) -> object:
        """
        this computes the age, and create a new object using the object constructor
        :return: a new object
        """
        age = date.today().year - birth_year

        return cls(name, age, job) # or Person(name, age, job)


# how to run class methods
new_person_object = Person.create_object_from_date_of_birth("Mara", 2011, "student")
print(new_person_object)
print(vars(new_person_object))