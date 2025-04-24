"""
* In Python there is also a possibility to use an unspecified (arbitrary) number of arguments, when the number of arguments is uncertain beforehand
* in this case , the arguments are specified as *args, and they are represented as a tuple
"""

def get_total_shopping_cart(*prices) -> float:
    """
    this is the docstring to document the function
    :param prices: an unspecified number of prices
    :return: the sum of prices in the shopping cart
    """

    total_shopping_cart = 0

    for price in prices:
        total_shopping_cart += price

    return total_shopping_cart


print(get_total_shopping_cart(25,100,150))
print(get_total_shopping_cart(25,100))