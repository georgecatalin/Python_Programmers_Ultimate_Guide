# in Python there is also possible to overload arithmetical operators for user type objects
# normally, arithmetic operators apply only to int, floor, str data types in Python
"""
The following functions have the be rewritten to achieve arithmetic operator overloading in Python:
1. + -> __add__(self,other)
2. - -> __sub__(self,other)
3. * -> __mul__(self, other)
4. / -> __div__(self,other)
5. // -> __floordiv__(self,other)
6. ** -> __pow__(self,other)
7. % -> __mod__(self,other)
8. += -> __iadd__(self,other)
9. -= -> __isub__(self,other)
10. *= -> __imul__(self,other)
11. /= -> __idiv__(self,other)
12. //= -> __ifloordiv__(self,other)
12. **= -> __ipow__(self,other)
13. %= -> __ipow__(self,other)
"""

class Transaction:
    """
    This is a model for Transaction
    """
    def __init__(self,amount, date_of_transaction):
        self.amount = amount
        self.date_of_transaction = date_of_transaction

    def __add__(self,other) -> int:
        return self.amount + other.amount

object_1 = Transaction(5100, "2024-12-31")
object_2 = Transaction(2200,"2025-04-29")

print("This is achieved through arithmetic operator overloading: ", object_1 + object_2)