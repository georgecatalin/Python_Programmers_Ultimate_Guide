# in Python when the child(derived) class does not have a specific constructor, then it makes use of the constructor in the parent(super/base) class
# in case when the child class has a constructor, the constructor of the child class is run firstly, then you have to call explicitely the constructor of the parent class

class Employee:
    """
    this is the Employee model
    """
    def __init__(self, full_name, job):
        self.full_name = full_name
        self.job = job


class  Developer(Employee):
    """
    this is the Developer class derived from the Employee class
    """
    def __init__(self,full_name, job, skill):
        """
        this is the constructor of the Child Class
        :param full_name:
        :param job:
        :param skill:
        """
        self.skill = skill
        Employee.__init__(self, full_name, job) # explicitly call the constructor of the Base Class in the constructor of the Child Class


class Manager(Employee):
    """
    This is the Model of the Manager
    """
    def __init__(self, full_name, job, departments):
        """
        This is the constructor of the child class
        :param full_name:
        :param job:
        :param departments:
        """
        self.departments = departments
        Employee.__init__(self, full_name, job)

        


employee_1 = Employee("George", "manager")
print(vars(employee_1))

developer_1 = Developer("Mara", "full stack developer", ["Python", "C"])
print(vars(developer_1))

manager_1 = Manager("Sorina", "COO", ["Accounting", "Marketing"])
print(vars(manager_1))