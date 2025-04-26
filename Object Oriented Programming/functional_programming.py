# the drawback of procedural programming is that it executes only from top to bottom and that is is not reusable
# functional programming mitigates this by achieving reusability through functions that can appeal one to each other


username = None
password = None

def accept_username() -> bool:
    """
    this is docstring
    :return:
    """
    global  username
    username = input("Enter your username= ")

    if username.isalnum(): # isalnum() checks if digit or character
        return True
    else:
        return False


def accept_password() -> bool:
    """
    this is docstring
    :return:
    """

    global  password

    password = input("Enter your password= ")

    if len(password) > 3:
        return True
    else:
        return False

def verify_login(uname : str, pwd : str) -> bool:
    """
    this is docstring
    :param uname:
    :param pwd:
    :return:
    """

    if uname == "admin" and pwd == "pass":
        return True
    else:
        return False


def login() -> None:
    """
    This is the docstring
    :return:
    """


    if not accept_username():
        print("Username should have only digits and characters")
    if not accept_password():
        print("You have entered a password shorter than necessary")

    if verify_login(username,password):
        print("You are logged in")
    else:
        print("Your login is not correct, pal")

login()
