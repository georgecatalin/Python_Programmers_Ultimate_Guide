# in Python we might also have needs to group objects into lists so that we can use loops and list comprehensions

class Product:
    """
    this is a model class for the product
    """
    def __init__(self, product_name, price, brand):
        self.product_name = product_name
        self.price = price
        self.brand = brand

products = [
Product("Air conditioner", 1900, "Whirlpool"),
Product("laptop", 5600, "Dell"),
Product("tablet", 1000, "Lenovo"),
]

print(products) # [<__main__.Product object at 0x00000166fcb6a350>, <__main__.Product object at 0x00000166fc95b0d0>, <__main__.Product object at 0x00000166fcb6a390>]

for product in products:
    print(vars(product))
"""
{'product_name': 'Air conditioner', 'price': 1900, 'brand': 'Whirlpool'}
{'product_name': 'laptop', 'price': 5600, 'brand': 'Dell'}
{'product_name': 'tablet', 'price': 1000, 'brand': 'Lenovo'}
"""

list_comprehension = [ (product.product_name, product.brand) for product in products if product.price > 1000]

print(list_comprehension) # [('Air conditioner', 'Whirlpool'), ('laptop', 'Dell')]

for item in list_comprehension:
    print(item)

"""
('Air conditioner', 'Whirlpool')
('laptop', 'Dell')
"""