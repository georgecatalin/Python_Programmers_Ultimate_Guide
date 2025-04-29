# in Python one can also overload the bool() function for user data types by writing the function __bool__(self)

class Transaction:
    """
    This is a model for Transaction
    """
    def __init__(self, amount, date):
        print("Hello from __init__ of Transaction class")
        self.amount = amount
        self.date = date

    def __bool__(self):
        return self.amount > 0

transaction_1 = Transaction(4000, "2025-03-10")
transaction_2 = Transaction(0, "2025-05-01")

print("Overloading the bool() ->", bool(transaction_1))
print("Overloading the bool() ->", bool(transaction_2))