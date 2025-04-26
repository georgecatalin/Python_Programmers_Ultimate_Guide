# methods are functions that are executed inside a class
# instance methods are meant to manipulate objects created with the class model

class Employee():
    print("Hello from class Employee") # this is executed automatically by the application  without the need to create any object

    def __init__(self, full_name, age, job):
        self.full_name = full_name
        self.age = age
        self.job = job
        self.organization = "Learning Co."

    def change_job(self,new_job):
        print("Hello from inside the change_job() method")
        self.job = new_job


employee_1 = Employee("George Calin", 46, "Manager")  # automatically appeals to Employee>__init__(object1, "George Calin", 46, "Manager"
employee_2 = Employee(full_name="Mara Calin", age=14, job="Software Developer")

print("object1 details", employee_1) # object1 details <__main__.Employee object at 0x000001a39993a550>
print("object2 details", employee_2) # object2 details <__main__.Employee object at 0x000001a39974b0d0>

employee_1.change_job("Body guard")
print("object1 details", employee_1) # object1 details <__main__.Employee object at 0x000001a39993a550> # the address of the object remains the same
print(vars(employee_1))

Employee.change_job(employee_1,"UX Designer") # this is an equivalent form of calling the instance method on employee_1 object
print("object1 details", employee_1) # object1 details <__main__.Employee object at 0x000001a39993a550> # the address of the object remains the same
print(vars(employee_1))