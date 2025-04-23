this_global_variable = 1978
print(f"From outside the function {this_global_variable}")

def this_function() -> None:
    """
    Here is the docstring for documentation
    :return:
    """
    this_local_variable = 2011 # this variable is only accessible inside the function body. it is reinitialized everytime the function gets appealed to


    print(f"From inside the function {this_global_variable}")
    # print(y) # NameError: name 'y' is not defined

this_function()

y = 1954 # a global variable is accessible in whole python file, that includes also functions which follow after the place where the variable was defined