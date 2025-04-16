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

this_frozen_set = frozenset(european_countries)

print(f"display the frozenset: \n {this_frozen_set}")
print(type(this_frozen_set)) # <class 'frozenset'>
print(len(this_frozen_set)) # 51

# A frozenset is a special type of set which is unordered, unindexable and unduplicatable , but unlike the normal sets, a frozen set is immutable
# that means one can not modify elements, items or objects in a frozenset, or add new elements or remove elements from a frozenset

# this_frozen_set.add("Uganda") # AttributeError: 'frozenset' object has no attribute 'add'