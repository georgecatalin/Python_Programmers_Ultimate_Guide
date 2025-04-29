# in Python MRO stands for Method Resolution Order and represents the order in which methods are executed
# Python uses the following algorithm for MRO : Depth first, and then left to right e.g D->A,B,C-> object we have D,A,B,C, object

class DebitTransaction:
    """
    This is a model for Debit Transaction
    """
    def __init__self(self, debit_transaction_id, amount):
        print("__init__(self) in DebitTransaction")
        self.debit_transaction_id = debit_transaction_id
        self.amount = amount

class CreditTransaction:
    """
    This is a model for Credit Transaction
    """
    def __init__(self, credit_transaction_id, amount):
        print("__init__(self) in CreditTransaction")
        self.credit_transaction_id = credit_transaction_id
        self.amount = amount

class FundsTransfer(DebitTransaction, CreditTransaction):
    """
    This is a model for Funds Transfer
    """
    def __init__(self,debit_transaction_id, credit_transaction_id, amount, date_of_transfer):
        print("__init__(self) in FundsTransfer")
        super(FundsTransfer,self).__init__(debit_transaction_id, amount) # DebitTransfer class as per the MRO order
        super(DebitTransaction,self).__init__(credit_transaction_id, amount) # CreditTransfer class as per the MRO order
        self.date_of_transfer = date_of_transfer



#print the Method Resolution Order as per Python algorithm
print(FundsTransfer.mro())

funds_transfer_object = FundsTransfer(1234, 2342, 34000, "2025-05-01")
print(vars(funds_transfer_object))