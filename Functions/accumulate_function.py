# unlike when using the reduce() function out of functools module, the accumulate() function from itertools module outputs a list containing all accumulators up to the last one
# the reduce() function was outputting only the last accumulator

from itertools import  accumulate

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
    {"full name": "Tomáš Horák", "age": 28, "job": "Backend Developer", "salary": 71000}
]

def add_salary(accumulator, current):
    """
    This is the docstring to document the function
    :param accumulator: something here
    :param current: something here
    :return: something here
    """
    print("accumulator= ", accumulator, " current object= ", current)
    return accumulator + current["salary"]

the_accumulator_object = accumulate(employees,add_salary, initial=0) # but the add_salary() function is not run, yet until transformed to list()
print("*"  * 50)
print("The total of salaries calculated with the accumulate() function is \t ->", the_accumulator_object )
print(list(the_accumulator_object))

# express the same with lambda

the_accumulator_object_with_lambda= accumulate(employees, lambda accumulator, current: accumulator + current["salary"], initial=0)
print("The list expressed with accumulate() through lambda expression :")
print(list(the_accumulator_object_with_lambda))