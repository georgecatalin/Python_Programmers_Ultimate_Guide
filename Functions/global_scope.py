# global variable can pe printed from any functions after the moment they have been declared in the code
# global variable needs "global" accessor to be able to be modified inside functions, otherwise the function create variables with the same name locally to their block


this_global_variable_1 = 1978
this_global_variable_2 = 2011

print(f"From outside the function global var 1 {this_global_variable_1}")
print(f"From outside the function global 2 {this_global_variable_2}")

def this_function() -> None:
    """
    this is the docstring of the function
    :return:
    """
    this_global_variable_1 = 1954 # a new local variable is created with the same name as the global
    print(f"From inside the function local var 1 {this_global_variable_1}")

    global this_global_variable_2
    this_global_variable_2 = 1977 # the global variable is modified inside the function cause it was noticed with global keyword before
    print(f"From inside the function global var 2 {this_global_variable_2}")

this_function()