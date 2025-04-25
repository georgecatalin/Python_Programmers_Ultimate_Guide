employees = [
    {"full name": "Alice Morgan", "age": 28, "job": "Software Developer", "salary": 72000},
    {"full name": "Bob Thompson", "age": 35, "job": "System Analyst", "salary": 68000},
    {"full name": "Carla Ruiz", "age": 30, "job": "HR Specialist", "salary": 61000},
    {"full name": "Daniel Nguyen", "age": 32, "job": "Network Engineer", "salary": 70000},
    {"full name": "Elena Petrova", "age": 29, "job": "Data Scientist", "salary": 88000},
    {"full name": "Frank Müller", "age": 40, "job": "IT Support", "salary": 54000},
    {"full name": "Grace Kim", "age": 27, "job": "UX Designer", "salary": 63000},
    {"full name": "Hassan Ali", "age": 34, "job": "DevOps Engineer", "salary": 95000},
    {"full name": "Isabella Rossi", "age": 38, "job": "Marketing Manager", "salary": 72000},
    {"full name": "Jack O’Neill", "age": 31, "job": "QA Tester", "salary": 58000},
    {"full name": "Katarina Novak", "age": 33, "job": "Business Analyst", "salary": 75000},
    {"full name": "Leo Schmidt", "age": 26, "job": "Frontend Developer", "salary": 66000},
    {"full name": "Maria Lopez", "age": 37, "job": "Project Manager", "salary": 88000},
    {"full name": "Nikos Papadakis", "age": 41, "job": "Database Administrator", "salary": 87000},
    {"full name": "Olga Ivanova", "age": 29, "job": "Technical Writer", "salary": 59000},
    {"full name": "Paul Brown", "age": 30, "job": "Mobile Developer", "salary": 73000},
    {"full name": "Quinn Lee", "age": 36, "job": "Security Analyst", "salary": 81000},
    {"full name": "Ravi Sharma", "age": 39, "job": "Cloud Architect", "salary": 112000},
    {"full name": "Sophie Dubois", "age": 35, "job": "Scrum Master", "salary": 79000},
    {"full name": "Tomáš Horák", "age": 28, "job": "Backend Developer", "salary": 770000}
]


def add_salaries_recursion(my_list: list) -> int:
    """
    this function calculates the sum of salaries through recursion in a list with dictionary objects
    :param my_list: a list of dictionaries
    :return: an int value that holds the sum of salaries
    """
    if not my_list:
        return 0
    else:
        return my_list[0]["salary"] + add_salaries_recursion(my_list[1:])


def get_max_salary_recursion_ver_1(my_list:list) -> int:
    """
    gets the maximum salary of a list using recursion
    :param my_list:
    :return:
    """
    if not my_list:
        return 0
    else:
        return max(my_list[0]["salary"],get_max_salary_recursion_ver_1(my_list[1:]))


def get_max_salary_recursion_ver_2(my_list: list) -> int:
    """
    this function gets the maximum salary from a list of dictionaries using if else
    :param my_list:
    :return:
    """
    if not my_list:
        return 0
    else:
        if my_list[0]["salary"] >= get_max_salary_recursion_ver_2(my_list[1:]):
            return my_list[0]["salary"]
        else:
            return get_max_salary_recursion_ver_2(my_list[1:])



print("the sum of salaries by recursion is ", add_salaries_recursion(employees))
print("the max of salaries by recursion with version 1 is ", get_max_salary_recursion_ver_1(employees))
print("the max of salaries by recursion with version 2 is ", get_max_salary_recursion_ver_2(employees))


