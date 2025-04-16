eu_countries = {
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
    "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
    "Spain", "Sweden"
}

print("The set is \t ->", eu_countries)

# remove "Romania"
eu_countries.remove("Romania")
print("The set after removing \t ->", eu_countries)

# remove an element which does not exist in the set
# eu_countries.remove("India") # KeyError: 'India' at all times make sure the element exists before trying to reove it with .remove()
print("The set after removing \t ->", eu_countries)

# remove "Italy"
eu_countries.discard("Italy")
print("The set after removing \t ->", eu_countries)

# remove an element which does not exist in the set with discard()
eu_countries.discard("China") # this does not return error
print(" eu_countries.discard('China') \t ->", eu_countries)

# clear the entire set
eu_countries.clear()
print(" eu_countries.clear() \t ->", eu_countries)

# delete completely the reference variable
del eu_countries
