class Employee():
    print("Hello from class Employee") # this is executed automatically by the application  without the need to create any object

    def __init__(self, full_name, age, job):
        self.full_name = full_name
        self.age = age
        self.job = job
        self.organization = "Learning Co."


employee_1 = Employee("George Calin", 46, "Manager")  # automatically appeals to Employee>__init__(object1, "George Calin", 46, "Manager"
employee_2 = Employee(full_name="Mara Calin", age=14, job="Software Developer")

print("object1 details", employee_1) # object1 details <__main__.Employee object at 0x000001a39993a550>
print("object2 details", employee_2) # object2 details <__main__.Employee object at 0x000001a39974b0d0>

print(vars(employee_1)) # {'full_name': 'George Calin', 'age': 46, 'job': 'Manager', 'organization': 'Learning Co.'}
print(vars(employee_2)) # {'full_name': 'Mara Calin', 'age': 14, 'job': 'Software Developer', 'organization': 'Learning Co.'}