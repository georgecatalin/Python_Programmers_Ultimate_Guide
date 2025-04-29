# in Python we use setter methods to validate the values before being passed to the instance attributes
from Tools.scripts.summarize_stats import emit_execution_counts


class Person:
    """
    This is a model for Person
    """
    def __init__(self, full_name, email_address):
        self.set_full_name(full_name) # we use setter methods to pass the values to instance attributes
        self.set_email_address(email_address) # we use setter methods to pass the values to instance attributes

    def set_full_name(self, value):
        """
        this validates before passing to instance attribute
        :param value:
        :return:
        """
        if isinstance(value,str) and len(value) > 3:
            self.full_name = value
            print("Full Name is valid")
        else:
            print("Full name is invalid")
            self.full_name = None

    def set_email_address(self,value):
        """
        This is the setter for the email_address instance attribute
        :param value:
        :return:
        """
        if isinstance(value, str) and value.find(".") > 0 and value.find("@") > 0:
            self.email_address = value
            print("Email Address is valid")
        else:
            print("Email Address is not valid")
            self.email_address = None

person_1 = Person("Co", "sd fd")
print(vars(person_1))

person_2 = Person("Mara", "mara@email.ro")
print(vars(person_2))