"""
* in Python the arguments for functions can be specified as either positional arguments where these are in the order of the function definition
or as keyword arguments (kwargs) when the order of the parameters does not matter as long as the name of the parameter is associated to the value
"""

def get_interest_value(amount:int, years:int, interest_rate:float) -> float:
    """
    this is the docstring to document the function
    :param amount: amount of currency
    :param year: number of years
    :param interest_rate: interest rate
    :return: the interest value to be paid to the person that makes the deposit
    """

    amount_to_pay = amount * years * interest_rate/100
    return  amount_to_pay


print(get_interest_value(125,5,50)) # this uses positional arguments
print(get_interest_value(interest_rate=35, amount=500, years = 10)) # this uses keyword arguments
print(get_interest_value(1000,interest_rate=45, years=30)) # this uses a mix from positional arguments and keyword arguments
# note that the positional arguments have to respect their order from the function definition body