def get_country() -> str:
    """
    Docstring here
    :return:
    """
    # appeal another function from inside a function here
    print(get_continent())
    print(get_continent())
    return "Romania"


def get_continent() -> str:
    """
    docstring here
    :return:
    """
    return "Europe"


print(get_continent()) # Europe
print(get_country()) #  Europe Europe Romania