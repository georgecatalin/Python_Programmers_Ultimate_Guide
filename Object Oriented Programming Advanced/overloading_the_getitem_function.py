"""
in Python we might overload the object[key] to a particular user type by writing it into the function __getitem__(self,key)
"""

class Sales:
    """
    This is a model for Sales
    """
    def __init__(self, asia_sales: list, europe_sales: list):
        self.asia_sales = asia_sales
        self.europe_sales = europe_sales

    def __len__(self):
        return len(self.asia_sales) + len(self.europe_sales)

    def __getitem__(self,key):
        combined_list = [* self.asia_sales, * self.europe_sales]
        return [element for element in combined_list if element["country"] == key][0]["amount"]


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
        {"country":"Spain", "amount": 250},

    ]
)


# we wish to extract the Sales by a syntax like new_object_1["China"] => result should be 250
print("This is obtained by overloading the getitem() function ->> \t new_object_1[\"India\"] = ", new_object_1["India"])