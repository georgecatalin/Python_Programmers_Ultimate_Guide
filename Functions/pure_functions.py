# the concept of pure functions appears in multiple programming languages lile Python, C#, Java
# Pure functions are desirable cause they are easily to be utilized in debugging, unit testing
# There are 5 features associated to pure functions:
#   pure functions do not depend on any external values like global variables, database values, values from files
#   pure functions depend solely on the arguments they are provided with
#   pure functions do not have side effects
#   pure functions do not modify the arguments, but they do something with the arguments
#   pure functions obtain identical results anytime when using the same arguments

def example_pure_function_sqr(n):
    """
    pure function here
    :param n:
    :return:
    """
    result = n * n
    return result


