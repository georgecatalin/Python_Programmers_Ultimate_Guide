name = "Mara"
email_address = None # we use None when the value of the variable is not available at the moment , and we can set it later

print("Boolean converted ",bool(name)) # True
print("Boolean converted ",bool(email_address)) # False

# how to check if both values are specified, that means they are not None for the time being
print("how to check if both values are specified, that means they are not None for the time being \t ->", bool(name) is None or bool(email_address) is None)


# there are two possibilities to check for None values, either with the == operator or with is None
# we prefer 'is None' because == operator might be overloaded in that class

