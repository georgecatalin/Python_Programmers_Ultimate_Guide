# we use the reduce() function to apply a single function to multiple objects and obtain a single final value
# syntax: myfunction(accumulator, current)
#  reduce(myfunction, iterator, initial_value_of_accumulator

from functools import reduce

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

def add_salaries(accumulator, current):
    """
    this is the docstring to document the function
    :param accumulator: blabla
    :param current: blabla
    :return: blabla
    """
    print(f"The accumulator is \t -> {accumulator}, and the current iteration object is \t -> {current}")
    return accumulator + current["salary"]

def get_longer_fullname(accumulator, current):
    """
    this is the docstring to document the function
    :param accumulator: something
    :param current: something
    :return: something
    """
    if len(accumulator) <= len(current["full name"]):
        accumulator = current["full name"]

    print(f"The accumulator is \t -> {accumulator}:{len(accumulator)}, and the current iteration object is \t -> {current}:{len(current["full name"])}")

    return accumulator

print("The sum of salaries calculated with reduce() function is \t ->", reduce(add_salaries,employees,0))

print("The largest full name in the collection of objects is ", reduce(get_longer_fullname,employees))

# write the reduce() function using nameless(lambda functions)
# note that the nameless functions(lambda) can contain only a single statement inside

print("The sum of salaries calculated with  LAMBDA reduce() function is \t ->",
      reduce(
          lambda accumulator, current: accumulator + current["salary"],
          employees,
          0))

print("The largest full name in the collection of objects is WITH LAMBDA ",
      reduce(
          lambda accumulator, current : current["full name"] if len(accumulator) <= len(current["full name"]) else accumulator,
          employees
      ))