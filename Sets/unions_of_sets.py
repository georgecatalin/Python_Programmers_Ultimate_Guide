top_populated_countries = {
    "China", "India", "United States", "Indonesia", "Pakistan",
    "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico"
}

top_largest_countries = {
    "Russia", "Canada", "China", "United States", "Brazil",
    "Australia", "India", "Argentina", "Kazakhstan", "Algeria"
}


print(f"first set :\n{top_populated_countries}")
print(f"second set :\n{top_largest_countries}")

all_countries = top_populated_countries.union(top_largest_countries)
print(f"The union of the two sets adds the elements from a set to another set, but keeps them only unique if they appear twice in both sets. \n {all_countries}")

# instead of the .union() method, one can use the union operator (Python 3.9+)
all_countries_union_op = top_largest_countries | top_populated_countries
print(f"Union with union operator: \n {all_countries_union_op}") # order of items is random, upon display

# the sets are not modified, only a new set is created for the union in both previous cases
print(f"first set :\n{top_populated_countries}")
print(f"second set :\n{top_largest_countries}")


# how to join with modification of the set
print("how to join with modification of the set")
top_populated_countries.update(top_largest_countries)
print(f"first set :\n{top_populated_countries}")
print(f"second set :\n{top_largest_countries}")