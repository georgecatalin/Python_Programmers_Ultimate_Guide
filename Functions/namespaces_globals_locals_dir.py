# a Python file is often called as a module
# A namespace is a dictionary object which holds the set of variables within that scope
# There exist 3 namespaces in Python: 1. built-in namespace (for Python functions,etc), 2.global namespace (for each file), 3. local namespace (for each function)


this_global_variable_1 = 1978
this_global_variable_2 = 2011

# we use globals() function to print the dictionary object holding all the global variables in the current Python module
print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F7B2694380>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Training\\Python_Programmers_Ultimate_Guide\\Functions\\namespaces_globals_locals_dir.py', '__cached__': None, 'this_global_variable_1': 1978, 'this_global_variable_2': 2011}

def this_function() -> None:
    """
    this is the docstring to document the function
    :return:
    """
    this_local_variable_1 = 1954
    this_local_variable_2 = 1953

    # we use locals() to display the dictionary object that holds the set of all local variables
    print(locals()) # {'this_local_variable_1': 1954, 'this_local_variable_2': 1953}

    # we use dir() function to display a list object that holds the names of the local variables
    print(dir()) # ['this_local_variable_1' , 'this_local_variable_2']

this_function()

print(locals()) # if we use locals() outside the function ,it will deliver the same result as globals()