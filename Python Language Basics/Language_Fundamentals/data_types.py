# in Python, anything is an object and that includes also the values which are objects of the data types (classes)
# data types in Python:  int, float, complex, str and bool

int_object = 10
print("Prove it is an object of its data type ->", type(int_object))
print("Is instance of the class ->", isinstance(int_object,int))

float_object = 3.141567
print("Prove it is an object of its data type ->", type(float_object))
print("Is instance of the class ->", isinstance(float_object,float))

complex_object = 10 + 3j # used in applications for electricity
print("Prove it is an object of its data type ->", type(complex_object))
print("Is instance of the class ->", isinstance(complex_object,complex))

bool_object = True
print("Prove it is an object of its data type ->", type(bool_object))
print("Is instance of the class ->", isinstance(bool_object,bool))

str_object = "Zizou"
print("Prove it is an object of its data type ->", type(str_object))
print("Is instance of the class ->", isinstance(str_object,str))