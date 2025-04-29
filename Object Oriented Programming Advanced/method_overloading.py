# method overloading means writing multiple functions/methods with the same name , but different parameters
# method overloading is not supported in Python by default, unlike in other programming languages like C# or Java
# in Python one needs to import the module 'multipledispatch'

from multipledispatch import dispatch

class InterestCalculator:
    """
    The model for interest calculator
    """

    @dispatch(int, int, int)  # we use the dispatch decorator to specify what types of parameters we expect
    def get_simple_interest(self, principal, rate_of_interest, number_of_years):
        return (principal * rate_of_interest * number_of_years)/100

    @dispatch(int,int) # we use the dispatch decorator to specify what types of parameters we expect
    def get_simple_interest(self, yearly_interest, number_of_years): # the method has the same name, but a different number of parameters, and data type of parameters might differ
        return  yearly_interest * number_of_years


this_interest = InterestCalculator()
print(this_interest.get_simple_interest(1000,10,20)) #  =1000 * 10 *20 /100 =   2000.0
print(this_interest.get_simple_interest(10, 200)) # 10 * 200 = 2000

"""
without importing 'multipledispatch' module, method overloading is not supported. 
the second form of the method, the one with two arguments has overwritten the first one -> TypeError: InterestCalculator.get_simple_interest() takes 3 positional arguments but 4 were given
"""