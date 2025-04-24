# when speaking about functions, the parameters are the variables that take the values represented as arguments
# a function is a collection of statements that achieve a certain task

# problem -> computer interest value
# interest_value = amount * years * interest_rate/100

def get_interest_value(amount : int = 1000, years : float = 1.0, interest_rate : float = 25) -> float :
    """
    here is the docstring to document the function
    :param amount: the amount in currency
    :param years: the number of years of the deposit
    :param interest_rate: the interest rate
    :return: the value of the interest to be paid
    """

    value = None
    value = amount * years * interest_rate/100
    return  value


interest_value_1 = get_interest_value() # 1000, 1.0, 25
print(f"interest_value_1 = {interest_value_1}")

interest_value_2 = get_interest_value(2000) # 2000, 1.0, 25
print(f"interest_value_2 = {interest_value_2}")

interest_value_3 = get_interest_value(2000,1.5) # 2000, 1.5, 25
print(f"interest_value_3 = {interest_value_3}")

interest_value_4 = get_interest_value(2000,1.5, 40) # 2000, 1.5, 40
print(f"interest_value_4 = {interest_value_4}")
