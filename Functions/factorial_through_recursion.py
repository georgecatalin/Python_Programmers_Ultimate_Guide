# recursion is the concept when a function makes use of itself when a condition is true

def get_factorial_through_recursion(n:int) -> int:
    """
    the docstring for documentation of the function is here
    :param n:
    :return:
    """
    if n <= 1: # this is the ending condition
        return 1
    else:
        return n * get_factorial_through_recursion(n-1)

print(get_factorial_through_recursion(1))
print(get_factorial_through_recursion(4)) # 1*2*3*4 = 24