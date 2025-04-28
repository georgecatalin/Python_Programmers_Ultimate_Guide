# inheritance in Python, as long as in all other programming languages supports the concept of "is_type_of"


class Person: # this is the Parent, Base or SuperClass
    """
    This is the model of a Person
    """
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def get_details(self):
        """
        this is an instance method
        :return:
        """
        print(f"The name is {self.full_name} and the email is {self.email}.")

# all the instance attributes from the base class and the instance method from the base class can be reused in the child class
class Developer(Person): # Developer Class inherits from Person Class, Developer is a Child Class or a Derived Class
    pass

class Manager(Person): # Manager Class inherits from Person Class, Manager is a Child Class or a Derived Class
    pass

person = Person("George Calin", "george_catalin@yahoo.com")
print(vars(person))
person.get_details()

child_1 = Developer("Mara Calin", "mara@yahoo.com")
child_1.skills = ["Python", "C#"] # additionally instance attributes can be added to objects, after the object was constructed in Python
print(vars(child_1))
child_1.get_details()

child_2 = Manager("Sorina", "sorina@email.com")
child_2.location = ["Romania", "United States"]
print(vars(child_2))
child_2.get_details()