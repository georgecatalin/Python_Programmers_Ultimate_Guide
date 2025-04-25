def  get_factorial(n: int)-> int:
    """
    this function computes the factorial
    :param n:
    :return:
    """
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i

    return  factorial

def get_factorial_ver_2(n:int) -> int:
    """
    the for loops is downwards
    :param n:
    :return:
    """
    factorial = 1
    for i in range(n,0,-1):
        factorial =  factorial * i

    return factorial

print(f"Factorial() method 1 \t -> {get_factorial(9)}")
print(f"Factorial() method 1 \t -> {get_factorial_ver_2(9)}")