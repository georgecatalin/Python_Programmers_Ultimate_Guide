# in Python the code associated with the class definition is run by the application immediately
# although, the __init__() function is being executed only when a new object is created and it can be used to set instance attributes

class Employee:
    print("Hello from class Employee")
    def __init__(self):
        """
        This method is run anytime a new object is created, instead of "self" any other parameter name can be used, but 'self' is recommended
        """

        self.full_name = "Ronan the barbarian"
        self.age = 30
        self.salary = 45000


employee_1 = Employee() # automatically Employee.__init__(object) is run and the attributes are set into the object
print(vars(employee_1)) # {'full_name': 'Ronan the barbarian', 'age': 30, 'salary': 45000}

employee_2 = Employee() # objects are nameless, they are stored in the object pool of the arena (heap), and the reference variable 'employee_2' stores it memory address
print(vars(employee_2)) # {'full_name': 'Ronan the barbarian', 'age': 30, 'salary': 45000}
