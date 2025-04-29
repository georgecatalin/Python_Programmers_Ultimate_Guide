# in Python the str() can be overloaded for user defined types by rewriting the __str__(self) function

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

    def __str__(self):
        asian_countries_list = list(map(lambda item: item["country"], self.asia_sales))
        europe_coutries_list = list(map(lambda item: item["country"], self.europe_sales))
        all_countries = [*asian_countries_list, *europe_coutries_list]
        return " ; ".join(all_countries)


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


# we wish to be able to print a list of all countries when str(new_object_1)
print(str(new_object_1)) # is the same with print(new_object_1) # China ; India ; Russia ; Vietnam ; France ; UK ; Germany ; Spain
print("is similar with")
print(new_object_1) # China ; India ; Russia ; Vietnam ; France ; UK ; Germany ; Spain