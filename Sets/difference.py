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

print("*" * 50)
difference_through_method = top_populated_countries.difference(top_largest_countries)
print("The .difference() method does not modify the existing sets, but create a newer one")
print(f"'top_populated_countries' set : \n {top_populated_countries}")
print(f"'top_largest_countries' set : \n {top_largest_countries}")
print(f"The difference set : \n {difference_through_method}")

difference_through_operator =  top_populated_countries - top_largest_countries # Python 3.9 onwards
print("The difference() operator - does not modify the existing sets, but create a newer one")
print(f"'top_populated_countries' set : \n {top_populated_countries}")
print(f"'top_largest_countries' set : \n {top_largest_countries}")
print(f"The difference set : \n {difference_through_operator}")

# modify the set
top_populated_countries.difference_update(top_largest_countries)
print("top_populated_countries.difference_update(top_largest_countries)")
print(f"'top_largest_countries' set : \n {top_largest_countries}")
print(f"The top_populated_countries set was modified : \n {top_populated_countries}")