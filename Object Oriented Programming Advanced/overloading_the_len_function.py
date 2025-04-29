# In Python, by default the len() function can be applied to strings and collections (lists, tuples, sets, etc)
# If one tries to apply the len() function to a user type , then the interpreter will fetch an error cause if encounters an undefined situation

class Sales:
    """
    This is a model for Sales
    """
    def __init__(self, asia_sales: list, europe_sales: list):
        self.asia_sales = asia_sales
        self.europe_sales = europe_sales

    def __len__(self):
        return len(self.asia_sales) + len(self.europe_sales)


new_object_1 = Sales(
    [
        {"country":"China", "amount":250},
        {"country":"India", "amount": 50},
        {"country":"Russia", "amount":150},
        {"country":"Vietnam", "amount": 660},
    ],
    [
        {"country":"France", "amount": 100},
        {"country":"UK", "amount": 700},
        {"country":"Germany", "amount": 340},
        {"country":"Spain", "amount": 340},

    ]
)

print("This is obtained by overloading the __len__() function for a user type: ", len(new_object_1))