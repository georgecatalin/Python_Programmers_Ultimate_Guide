"""
- in Python there are two ways of making use of the return keyword:
    1. return -> and the execution of the code goes back to the calling portion
    2. return some_value -> some_value is returned after the execution of the code

"""

def print_employee() -> str:
    """
    This function prints the employee name
    :return:
    """
    return "George Calin"


print(print_employee()) # it is recommended to leave 2 blank lines after each function block or class block of code in Python
    