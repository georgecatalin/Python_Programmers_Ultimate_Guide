class Person:
    """
    This is the model for Person
    """
    def __init__(self, full_name, gender):
        self.full_name = full_name
        self.gender = gender

    def get_full_name(self):
        title = "Mr. " if self.gender == "Male" else "Ms. "
        return title + self.full_name


person_1 = Person("George", "Male")
print(person_1.get_full_name())

# in general, as a rule of good practice it is recommended to create a getter and a setter method for each instance attribute