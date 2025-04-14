cities = ["Galati", "Braila", "Focsani", "Constanta", "Brasov"]

# unpacking

city1, city2, city3, *other_cities = cities
print(city1) # "Galati"
print(city2) # "Braila"
print(city3) # "Focsani"
print(other_cities) # ["Constanta", "Brasov"]