# Python  is a programming language which support all three programming paradigms:
# procedural programming
# functional programming
# object oriented programming

"""
Procedural programming paradigm:
    code is executed top to bottom
    one can use loops, decision statements and collections
"""

username = None
password = None

username = input("Enter your username = ")
password = input("Enter your password = ")

if username == "admin" and password == "pass":
    print("You are logged in")
else:
    print("Login failed")