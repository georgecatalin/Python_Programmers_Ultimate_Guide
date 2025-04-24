# we can use the map(function_name, iterable) anytime we wish to modify each element of an iterable
# alternatively we can use the map function with a lambda (nameless function) like map(lambda_function, iterable)


employees = [
    {"complete name": "Alice Morgan", "job": "Software Developer", "age": 28, "date of employment": "2019-06-15"},
    {"complete name": "Bob Thompson", "job": "System Analyst", "age": 35, "date of employment": "2017-03-22"},
    {"complete name": "Carla Ruiz", "job": "HR Specialist", "age": 30, "date of employment": "2020-09-01"},
    {"complete name": "Daniel Nguyen", "job": "Network Engineer", "age": 32, "date of employment": "2018-11-10"},
    {"complete name": "Elena Petrova", "job": "Data Scientist", "age": 29, "date of employment": "2021-01-18"},
    {"complete name": "Frank Müller", "job": "IT Support", "age": 40, "date of employment": "2015-08-03"},
    {"complete name": "Grace Kim", "job": "UX Designer", "age": 27, "date of employment": "2022-04-12"},
    {"complete name": "Hassan Ali", "job": "DevOps Engineer", "age": 34, "date of employment": "2019-12-09"},
    {"complete name": "Isabella Rossi", "job": "Marketing Manager", "age": 38, "date of employment": "2016-07-25"},
    {"complete name": "Jack O’Neill", "job": "QA Tester", "age": 31, "date of employment": "2020-02-05"},
    {"complete name": "Katarina Novak", "job": "Business Analyst", "age": 33, "date of employment": "2017-10-30"},
    {"complete name": "Leo Schmidt", "job": "Frontend Developer", "age": 26, "date of employment": "2022-06-07"},
    {"complete name": "Maria Lopez", "job": "Project Manager", "age": 37, "date of employment": "2015-05-13"},
    {"complete name": "Nikos Papadakis", "job": "Database Administrator", "age": 41, "date of employment": "2014-11-20"},
    {"complete name": "Olga Ivanova", "job": "Technical Writer", "age": 29, "date of employment": "2018-01-23"},
    {"complete name": "Paul Brown", "job": "Mobile Developer", "age": 30, "date of employment": "2019-04-19"},
    {"complete name": "Quinn Lee", "job": "Security Analyst", "age": 36, "date of employment": "2016-09-08"},
    {"complete name": "Ravi Sharma", "job": "Cloud Architect", "age": 39, "date of employment": "2013-03-17"},
    {"complete name": "Sophie Dubois", "job": "Scrum Master", "age": 35, "date of employment": "2018-08-14"},
    {"complete name": "Tomáš Horák", "job": "Backend Developer", "age": 28, "date of employment": "2021-11-29"},
    {"complete name": "Ursula Bennett", "job": "Software Developer", "age": 25, "date of employment": "2023-03-10"},
    {"complete name": "Victor Ortega", "job": "System Analyst", "age": 37, "date of employment": "2016-05-28"},
    {"complete name": "Wanda Schmidt", "job": "UX Designer", "age": 29, "date of employment": "2021-07-19"},
    {"complete name": "Xander Blake", "job": "Frontend Developer", "age": 27, "date of employment": "2022-10-01"},
    {"complete name": "Yasmin Rahman", "job": "QA Tester", "age": 32, "date of employment": "2020-12-15"},
    {"complete name": "Zachary Klein", "job": "Backend Developer", "age": 31, "date of employment": "2019-05-04"},
    {"complete name": "Anna Svensson", "job": "Data Scientist", "age": 30, "date of employment": "2020-02-27"},
    {"complete name": "Brian O'Reilly", "job": "IT Support", "age": 45, "date of employment": "2012-09-03"},
    {"complete name": "Clara Jensen", "job": "Project Manager", "age": 39, "date of employment": "2014-06-20"},
    {"complete name": "Diego Marquez", "job": "DevOps Engineer", "age": 33, "date of employment": "2021-01-09"}
]


def convert_job_to_upper(employee : dict) -> dict:
    """
    This is the docstring to document the function
    :param employee: a dictionary object with the employee properties
    :return: the modified dictionary object
    """
    print("Execute function for each element...")

    if employee["job"] != "Project Manager":
        employee["job"] =  employee["job"].upper()

    return  employee


new_object_convert = map(convert_job_to_upper, employees)
print(f"The object is \t -> {new_object_convert}") # the convert function is not executed for the moment for each element until the object is converted to an iterable object

new_list_convert = list(new_object_convert) # now the function to convert is executed for each object
print(new_list_convert)