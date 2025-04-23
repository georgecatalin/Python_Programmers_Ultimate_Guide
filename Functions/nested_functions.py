# when one wishes to split a larger task into much more smaller tasks, then one can use nested functions inside an outer function
# the nested functions are visible only inside the outer function where they have been created


def outer_function() -> None:
    print("Hello from outer function")

    def inner_function() -> None: # the nested function is only visible from inside the outer function where it was created
        print("Hello from the inner function")

    inner_function()


outer_function()