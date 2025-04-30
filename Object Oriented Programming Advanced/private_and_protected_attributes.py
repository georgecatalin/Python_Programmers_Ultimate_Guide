# Unlike other programming languages, Python does not quite support hiding attributes from outside the class through private and protected access modifiers
# in Python, the notion of 'private' and 'protected'  is rather a conventional notation of attributes to indicate fellow developers which attributes can be modified outside the class and which can not

class Employee():
    """
    This is the model for Employee
    """
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self._age = age # _age is the notation for protected attributes, so these can be accessed from the class and its children
        self.__gender = gender # __gender is the notation for private attributes, so these can only be accessed and set from inside their residing classes

employee_1 = Employee("Mara Calin", 14, "Female")
print(employee_1._age) # the interpreter warns about being a protected attribute, but it still shows it
print(vars(employee_1)) # {'full_name': 'Mara Calin', '_age': 14, '_Employee__gender': 'Female'}

#accessing the private attributes from outside the class
print(employee_1._Employee__gender)