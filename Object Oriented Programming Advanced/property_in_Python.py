class Employee:
    """
    This is the model for Employee
    """
    def __init__(self, full_name):
        self.__full_name = "Some Full Name"


    # write a getter method which you will transform afterwards into a property by adding the decorator '@property'
    @property
    def full_name(self):
        return  self.__full_name


    #write a setter method which you will transform afterwards into a property using the decorator '@full_name.setter'
    @full_name.setter
    def full_name(self,value):
        if isinstance(value,str) and value.isalnum():
            self.__full_name = value


    # write a deleter method which you will transform afterwards into a property using the decorator '@full_name.deleter'
    @full_name.deleter
    def full_name(self):
        del self.__full_name


employee = Employee("Something")
print(vars(employee))

# use the getter
print(employee.full_name)

# use the setter
employee.full_name = "GeorgeCalin"
print(employee.full_name)
print(vars(employee))

del employee.full_name

# print(employee.full_name) # AttributeError: 'Employee' object has no attribute '_Employee__full_name'