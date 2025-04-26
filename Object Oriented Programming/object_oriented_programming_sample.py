class Login():

    # in Python there is no such thing as fields or member variables.these have to be added with the __init__() function constructor only

    def __init__(self, username, password):
        if username.isalnum():
            self.username = username
        else:
            self.username = None
            print("The username should contain only characters and digits")

        if  len(password) > 6:
            self.password = password
        else:
            self.password = None
            print("The password should have more than 6 characters")


    def is_valid_login(self):
        return self.username == "admin" and self.password == "password1"  # each method can access all attributes of the objects
    """
    a shortened version for
    if uname == "uname" and pwd == "password1"
        return True
    else:
        return False
    """

uname = input("Enter your username: ")
pwd = input("Enter your password: ")

login_1 = Login(uname, pwd) # same as Login(login_1, uname, pwd)
print(login_1.is_valid_login())

