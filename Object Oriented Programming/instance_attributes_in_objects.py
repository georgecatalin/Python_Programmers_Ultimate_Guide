#  In Python instance attributes are the variables that can be stored in the objects
# the instance attributes can be created in both , the objects themselves and in the class as the model based upon which objects are created
# the drawback of creating attributes in the objects is the possibility of lack in consistency for naming such attributes

class Employee():
    print("Hello from class")

employee_1 = Employee()
employee_1.full_name = "George"
employee_1.age = 45

employee_2 = Employee()
employee_2.full_name = "Mara"
employee_2.age = 14

# how to print objects

print(f"Object1 details \t {employee_1}") # Object1 details 	 <__main__.Employee object at 0x000001da7e9b9ed0>
print(f"Object2 details \t {employee_2}") # Object2 details 	 <__main__.Employee object at 0x000001da7e7ab0d0>

# one can also print all the attributes associated with the objects by using the vars() function which creates a dictionary holding the key, value pairs
print(vars(employee_1)) # {'full_name': 'George', 'age': 45}
print(vars(employee_2)) # {'full_name': 'Mara', 'age': 14}