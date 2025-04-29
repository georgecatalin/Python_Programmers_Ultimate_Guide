# in Python MRO stands for Method Resolution Order and represents the order in which methods are executed
# Python uses the following algorithm for MRO : Depth first, and then left to right e.g D->A,B,C-> object we have D,A,B,C, object

class DebitTransaction:
    """
    This is a model for Debit Transaction
    """
    def __init__self(self, debit_transaction_id, amount, * args):
        print("enter __init__(self) in DebitTransaction")
        self.debit_transaction_id = debit_transaction_id
        self.amount = amount
        super(DebitTransaction, self).__init__(*args)  # CreditTransfer class as per the MRO order
        print("exit __init__(self) in DebitTransaction")

class CreditTransaction:
    """
    This is a model for Credit Transaction
    """
    def __init__(self, credit_transaction_id, amount, *args):
        print("enter __init__(self) in CreditTransaction")
        self.credit_transaction_id = credit_transaction_id
        self.amount = amount
        super(CreditTransaction,self).__init__() # goes to the next class as per the MRO , in this case it is object class
        print("exit __init__(self) in CreditTransaction")

class FundsTransfer(DebitTransaction, CreditTransaction):
    """
    This is a model for Funds Transfer
    """
    def __init__(self,debit_transaction_id, credit_transaction_id, amount, date_of_transfer):
        print(" enter __init__(self) in FundsTransfer")
        super(FundsTransfer,self).__init__(debit_transaction_id, amount, credit_transaction_id, amount) # DebitTransfer class as per the MRO order

        self.date_of_transfer = date_of_transfer
        print(" exit  __init__(self) in FundsTransfer")


#print the Method Resolution Order as per Python algorithm
print(FundsTransfer.mro())

funds_transfer_object = FundsTransfer(1234, 2342, 34000, "2025-05-01")
print(vars(funds_transfer_object))