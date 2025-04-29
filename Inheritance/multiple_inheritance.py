# in Python, unlike C# or Java, it is possible for a Child Class to inherit from multiple Parent Classes at once

class Debit_Transaction:
    """
    This is a model for Debit Transaction
    """
    def __init__(self, debit_transaction_id : int, debit_transaction_amount: int) -> None:
        self.debit_transaction_id = debit_transaction_id
        self.debit_transaction_amount = debit_transaction_amount


    def get_details(self):
        return f"Debit transaction id is {self.debit_transaction_id} and amount is {self.debit_transaction_amount}"

class Credit_Transaction:
    """
    This is a model for Credit Transaction
    """
    def __init__(self, credit_transaction_id: int, credit_transaction_amount: int) -> None:
        self.credit_transaction_id = credit_transaction_id
        self.credit_transaction_amount = credit_transaction_amount

    def get_details(self):
        return f"Credit transaction is is {self.credit_transaction_id} and amount is {self.credit_transaction_amount}"


class FundsTransfer(Debit_Transaction, Credit_Transaction): # this is multiple inheritance from multiple Parent Classes at once
    """
    This is a model for FundsTransfer
    """
    def __init__(self, debit_transaction_id : int, debit_transaction_amount: int, credit_transaction_id: int, credit_transaction_amount: int, date :str) -> None:
        Debit_Transaction.__init__(self, debit_transaction_id ,debit_transaction_amount)
        Credit_Transaction.__init__(self, credit_transaction_id, credit_transaction_amount)
        self.date = date


funds_transfer_reference_variable = FundsTransfer(2424, 45000, 224523, 45344, "2025=04-29")
print(vars(funds_transfer_reference_variable)) # {'debit_transaction_id': 2424, 'debit_transaction_amount': 45000, 'credit_transaction_id': 224523, 'credit_transaction_amount': 45344, 'date': '2025=04-29'}
