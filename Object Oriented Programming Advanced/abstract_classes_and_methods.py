# in Python , there might arise the need so certain methods to be enforced into implementation in child classes
# this can be achieved by setting the method as abstract, but since abstract methods can not live elsewhere than in abstract classes, so that classes have to be turned into abstract


from abc import ABC, abstractmethod

class Payment(ABC): # Any abstract class in Python must be a child of the class ABC which resides inside the abc module abc stands for 'abstract base class'
    """
    this is an abstract class
    """
    @abstractmethod # one needs the @abstractmethod decorator to mark any abstract method. abstract methods do not contain method body, as this will be implemented in children classes
    # this abstract method is going to force its implementation in the children classes
    def get_bill_value(self):
        pass

class CashPayment(Payment):
    def get_bill_value(self):
        return 100

class CreditCardPayment(Payment):
    def get_bill_value(self):
        return 200


object_1 = CashPayment()
print(object_1.get_bill_value())

object_2 = CreditCardPayment()
print(object_2.get_bill_value())