america_countries = {"United States", "Brazil", "Canada"}

top_largest_countries = {
    "Russia", "Canada", "China", "United States", "Brazil",
    "Australia", "India", "Argentina", "Kazakhstan", "Algeria"
}

print(f"'top_populated_countries' set : \n {america_countries}")
print(f"'top_largest_countries' set : \n {top_largest_countries}")

print(f"Issubset() \t -> {america_countries.issubset(top_largest_countries)}") # True
print(f"Issuperset() \t -> {top_largest_countries.issuperset(america_countries)}") # True
print(f"Isdisjoint() \t -> {america_countries.isdisjoint(top_largest_countries)}") # False because they contain at least one common element

european_countries = {
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan",
    "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria",
    "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia",
    "Finland", "France", "Georgia", "Germany", "Greece",
    "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan",  # Kazakhstan is transcontinental
    "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands",
    "North Macedonia", "Norway", "Poland", "Portugal", "Romania",
    "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia",
    "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine",
    "United Kingdom", "Vatican City"
}

north_american_countries = {
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada",
    "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador",
    "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica",
    "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago",
    "United States"
}

print(f"A set containing all countries in Europe: \n {european_countries}")
print(f"\n\nA set containing all countries in North America: \n {north_american_countries}")

print(f"\n\nA set containing 'north_american_countries.isdisjoint(european_countries)': \n {north_american_countries.isdisjoint(european_countries)}")
# True, because these sets do not have any common element


