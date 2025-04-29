# in Python , when a Child Class (Derived Class) inherits from a single Parent Class (Super Class or Base Class) this is called simple or single inheritance
# on the other hand, when a Child Class inherits from a Child Class which inherits from a Parent Class, this is called multilevel inheritance

class Transaction:
    """
    This is a model class for Transaction
    """
    def __init__(self, transaction_code, transaction_amount):
        self.transaction_code = transaction_code
        self.transaction_amount = transaction_amount


class Debit_Processing(Transaction):
    """
    This is a model for Debit_Processing
    """
    def __init__(self, transaction_code, transaction_amount, debit_id):
        super().__init__(transaction_code,transaction_amount)
        self.debit_id = debit_id


class Bill_Payment(Debit_Processing):
    """
    This is a model for Bill Payment
    """
    def __init__(self, transaction_code : str, transaction_amount : int, debit_id : str, biller_name : str) -> None:
        super().__init__(transaction_code, transaction_amount, debit_id)
        self.biller_name = biller_name


bill_payment_object = Bill_Payment("1121443",234555, "2311","Mara Calin")
print(vars(bill_payment_object)) # {'transaction_code': '1121443', 'transaction_amount': 234555, 'debit_id': '2311', 'biller_name': 'Mara Calin'}