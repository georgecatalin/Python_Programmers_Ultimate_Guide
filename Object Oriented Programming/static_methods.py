# in Python there exist methods that apply only logically to a certain class, but these methods do not use neither class attributes , nor instance(object) attributes
# such methods are called static methods

class Product:
    """
    this is a model of the product
    """
    def __init__(self, product_name, product_price): # constructor method
        self.product_name = product_name
        self.product_price = product_price


    def get_discount(self) -> float : # since this method requires an object to be created beforehand, and applies to this object, this is an instance object
        return  self.product_price * 0.10

    @staticmethod #this decorator is required to mark individually independent methods
    def get_discount_based_on_price(price:float) -> float:
        """
        this calculates the discount based on the price, and does not need any object or class attribute
        :param price:
        :return: the discount
        """
        return price * 0.1


# how to use the static method

discount_through_static_method_1 = Product.get_discount_based_on_price(56000)
print("discount_through_static_method_1", discount_through_static_method_1 , sep="-->")
product_1 = Product("laptop", 56000)
discount_through_static_method_2 = product_1.get_discount_based_on_price(56000)
print("discount_through_static_method_2", discount_through_static_method_2 , sep="-->")

# how to use the instance method
discount_through_instance_method_1 = product_1.get_discount()
print("discount_through_instance_method_1",discount_through_instance_method_1 ,sep="-->" )

discount_through_instance_method_2 = Product.get_discount(product_1)
print("discount_through_instance_method_2",discount_through_instance_method_2 ,sep="-->" ) # used from the class syntax