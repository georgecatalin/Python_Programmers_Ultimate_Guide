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


# after applying symmetric difference, once can extract all the elements from both sets, but which are not common

# do not modify the existing sets
symmetric_difference_through_method = top_populated_countries.symmetric_difference(top_largest_countries)
print(f"The symmetric difference set contains all the elements from both sets, which are not common: \n {symmetric_difference_through_method}")

symmetric_difference_through_operator = top_populated_countries ^ top_largest_countries # Python 3.9 +
print(f"The symmetric difference set contains all the elements from both sets, which are not common: \n {symmetric_difference_through_operator}")

# modify the existing set
top_populated_countries.symmetric_difference_update(top_largest_countries)
print(f"'top_populated_countries' set  WAS MODIFIED : \n {top_populated_countries}")
print(f"'top_largest_countries' set : \n {top_largest_countries}")