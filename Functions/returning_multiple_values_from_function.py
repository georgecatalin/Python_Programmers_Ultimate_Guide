def get_employee_details() -> ():
    """
    docstring goes here to document the function
    :return:
    """
    return "George Calin", 46


print(type(get_employee_details())) # <class 'tuple'>
print(get_employee_details()) # ('George Calin', 46)

# get the first element of the tuple
print(get_employee_details()[0])
# get the second element of the tuple
print(get_employee_details()[1])