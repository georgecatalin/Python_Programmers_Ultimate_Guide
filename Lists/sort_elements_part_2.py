# these are examples for creating new list objects instead of modifying the existing list object
european_ford_models_1985_2000 = [
    "Ford Fiesta Mk2",        # 1983–1989
    "Ford Fiesta Mk3",        # 1989–1997
    "Ford Fiesta Mk4",        # 1995–2002
    "Ford Escort Mk3",        # 1980–1986
    "Ford Escort Mk4",        # 1986–1990
    "Ford Escort Mk5",        # 1990–1995
    "Ford Escort Mk6",        # 1995–2002
    "Ford Orion",             # 1983–1993
    "Ford Sierra",            # 1982–1993
    "Ford Sierra RS Cosworth",# 1986–1992
    "Ford Granada Mk3",       # 1985–1994
    "Ford Scorpio",           # 1985–1998
    "Ford Mondeo Mk1",        # 1993–2000
    "Ford Ka Mk1",            # 1996–2008
    "Ford Puma",              # 1997–2002
    "Ford Probe",             # 1994–1997
    "Ford Cougar",            # 1998–2002
    "Ford Maverick",          # 1993–1998
    "Ford Galaxy",            # 1995–2006
    "Ford Transit Mk3",       # 1986–2000
    "Ford Transit Mk4",       # 1994–2000
    "Ford P100",              # 1982–1993
    "Ford RS200",             # 1984–1986
]

print("The initial list is -> \t", european_ford_models_1985_2000)

new_list_sorted_ascending = sorted(european_ford_models_1985_2000)
print("The new list object is -> \t", new_list_sorted_ascending)
print("The initial list is not modified -> \t", european_ford_models_1985_2000)

new_list_sorted_descending = sorted(european_ford_models_1985_2000, reverse=True)
print("The new list object is -> \t", new_list_sorted_descending)
print("The initial list is not modified -> \t", european_ford_models_1985_2000)

new_list_sorted_descending_case_insensitive = sorted(european_ford_models_1985_2000, reverse=True)
print("The new list object is -> \t", new_list_sorted_descending_case_insensitive)
print("The initial list is not modified -> \t", european_ford_models_1985_2000)

# one can also reverse the order of elements in a list
## by creating a new list
new_list_reversed = reversed(european_ford_models_1985_2000)
print("The new list object is -> \t", list(new_list_reversed)) # a list() has to be applied to the iterator to make it listanle
print("The initial list is not modified -> \t", european_ford_models_1985_2000)

## by modifying the existing list
european_ford_models_1985_2000.reverse()
print("The initial list is  modified -> \t", european_ford_models_1985_2000)
