# By method overriding in Python we understand extending or replacing a method from the Parent Class in the Child Class with a method with the same name and parameters
# The method overriding the method from the Parent Class may or may not execute the method from the Parent Class

class Employee:
    """
    The model for Employee
    """
    def __init__(self,full_name, salary):
        self.full_name = full_name
        self.salary = salary

    def get_net_salary(self, allowance_percentage : int) -> float:
        """
        Get the net salary
        :param allowance_percentage:
        :return:
        """
        allowance_sum = self.salary * allowance_percentage/100 # any instance method can access all instance attributes
        net_salary = self.salary + allowance_sum
        return  net_salary


class Developer(Employee): # Developer Class is a Child Class of the Employee Parent Class
    """
    This is the model for Developer
    """
    def __init__(self, full_name : str, salary : int, appraisal_percentage: int):
        """
        this is the constructor of the Child Class
        :param full_name:
        :param salary:
        :param appraisal_percentage:
        :return:
        """
        self.appraisal_percentage = appraisal_percentage
        super().__init__(full_name,salary)


    def get_net_salary(self, allowance_percentage: int) -> float:
        """
        This method overrides the method with the same name and the same parameters from the Parent Class
        :param allowance_percentage: parameter to the method
        :return: the net salary
        """
        appraisal_amount = self.salary * self.appraisal_percentage/100
        net_salary = super().get_net_salary(allowance_percentage)
        return  net_salary + appraisal_amount


developer = Developer("George Calin", 1000, 15)
print(vars(developer))
print(developer.get_net_salary(20))