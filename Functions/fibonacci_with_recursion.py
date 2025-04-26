def get_fibbonaci_elements_of_the_list(index : int) -> int:
    """
    this is the function that calculates each element of the list containing the Fibonacci series
    :param index: the index of the element being calculated
    :return: the element
    """

    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return get_fibbonaci_elements_of_the_list(index - 1) + get_fibbonaci_elements_of_the_list(index - 2)


def get_fibonacci_list(n: int) -> list:
    """
    This is the function that builds the list of elements that adhere to the Fibonacci rule
    :param n:
    :return:
    """
    list_of_elements = [] 

    for i in range(n):
        list_of_elements.append(get_fibbonaci_elements_of_the_list(i))
    return list_of_elements


list_of_fibonacci_for_10 = get_fibonacci_list(10)
print("list of fibonacci is ", list_of_fibonacci_for_10)