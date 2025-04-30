"""
Each module should contain documentation about its content - either classes, variables or functions
each .py file is called a module in Python.
a module can call another module.
anytime when a module is imported in another module, the entire code in the imported module is executed, except classes, and functions
"""

# we access consequently all the elements from other modules here

import module_b
import module_c as C #accessing the module through an alias

from module_d import * #import all the elements inside the respective module

from module_e import Model_1, Model_2 # import precise elements in the module

print(module_b.get_car_brand() + " " + module_b.get_car_model())

print(C.full_name, C.age, sep="->")

object_1 = Person()
object_2 = Skills()
this_var = gears

object_e_1 = Model_1()
object_e_2 = Model_2()

