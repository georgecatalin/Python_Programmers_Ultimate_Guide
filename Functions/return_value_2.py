"""
- in Python there are two ways of making use of the return keyword:
    1. return -> and the execution of the code goes back to the calling portion
    2. return some_value -> some_value is returned after the execution of the code

"""

def compute_sum() -> int:
    """
    This function computes the sum of consecutive numbers  -> 1 + 2 + 3 + ... + n
    :return:
    """

    n = 8
    this_sum = 0
    for i in range(1, n + 1):
        this_sum += i

    return  this_sum

s = compute_sum()
print("The sum ", s)