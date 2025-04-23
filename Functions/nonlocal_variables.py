# the concept of nonlocal variables is rarely used in Python production applications, although it arises as interview questions
# 'nonlocal' concept is similar to 'global' concept, but refers to nested functions
# namely modifying a variable declared in the outer function inside the inner function


def outer_function() -> None:
    """
    This is the docstring to explain the function
    :return:
    Nothing
    """

    outer_variable_1 = 1978
    outer_variable_2 = 1977

    print(f"From outer function outer_variable_1 = {outer_variable_1}") # 1978
    print(f"From outer function outer_variable_2 = {outer_variable_2}") # 1977

    def inner_function() -> None:
        """
        This is the docstring to explain the function
        :return:
        Nothing
        """

        outer_variable_1 =  2011 # a new local variable in the inner function is created
        print(f"The local variable from inner function outer_variable_1 {outer_variable_1} ") # 2011

        nonlocal outer_variable_2 # specify that we refer to the 'outer_variable_2' from the outer_function, and we won't create a new variable locally with this name
        outer_variable_2 = 1954
        print(f"The  variable from inner function outer_variable_2 {outer_variable_2} ")  # 1954

    inner_function()

outer_function()