def is_valid_login(username : str, password : str) -> bool:
    """
    This is the docstring to document the function
    :param username: specify username
    :param password: specifu password
    :return: a boolean value
    """
    valid = None
    if username == "admin" and password == "this":
        valid = True
    else:
        valid = False

    return valid


user_input = input("Enter user name: ")
pass_input = input("Enter password: ")

login_ok = is_valid_login(user_input,pass_input)

if login_ok :
    print("You logged in correctly")
else:
    print("You did not log in correctly")