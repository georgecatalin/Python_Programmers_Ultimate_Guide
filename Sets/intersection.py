top_populated_countries = {
    "China", "India", "United States", "Indonesia", "Pakistan",
    "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico"
}

top_largest_countries = {
    "Russia", "Canada", "China", "United States", "Brazil",
    "Australia", "India", "Argentina", "Kazakhstan", "Algeria"
}

print(f"'top_populated_countries' set : \n {top_populated_countries}")
print(f"'top_largest_countries' set : \n {top_largest_countries}")

print("**" * 30)
all_common_countries_both_sets_intersection = top_populated_countries.intersection(top_largest_countries)
print("The .intersection() method does not modify the existing sets, but create a newer one")
print("**" * 30)
print(f"The intersection set using the .intersection() method: \n {all_common_countries_both_sets_intersection}")

# & is the intersection operator from Python 3.9 onwards
all_common_countries_both_sets_intersection_operator = top_populated_countries & top_largest_countries
print("**" * 30)
print("The intersection operator '&' does not modify the existing sets, but create a newer one")
print("**" * 30)
print(f"The intersection set using the intersection operator &: \n {all_common_countries_both_sets_intersection_operator}")

# intersection with modification of the set
top_populated_countries.intersection_update(top_largest_countries)
print(f"'top_populated_countries' set  was modified: \n {top_populated_countries}")
print(f"'top_largest_countries' set : \n {top_largest_countries}")