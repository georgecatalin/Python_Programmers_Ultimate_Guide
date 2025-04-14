car_brands = [
    "Toyota",
    "Honda",
    "Ford",
    "BMW",
    "Mercedes-Benz",
    "Volkswagen",
    "Audi",
    "Chevrolet",
    "Hyundai",
    "Nissan",
    "Kia",
    "Lexus",
    "Volvo",
    "Porsche",
    "Tesla"
]

print("The initial list is -> \t", car_brands)
#['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes-Benz', 'Volkswagen', 'Audi', 'Chevrolet', 'Hyundai', 'Nissan', 'Kia', 'Lexus', 'Volvo', 'Porsche', 'Tesla']

car_brands.sort() # sort ascending
print("The list after sorting is -> \t", car_brands)
# ['Audi', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Lexus', 'Mercedes-Benz', 'Nissan', 'Porsche', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']

car_brands.sort(reverse=True) # sort descending
print("The list after sorting descending is -> \t", car_brands)


car_brands_mixed_case = [
    "Toyota",
    "honda",
    "Ford",
    "bMW",
    "Mercedes-Benz",
    "Volkswagen",
    "Audi",
    "chevrolet",
    "Hyundai",
    "Nissan",
    "Kia",
    "lexus",
    "Volvo",
    "Porsche",
    "Tesla",
    "alfa-Romeo"
]

car_brands_mixed_case.sort() # sorting is performed by the ASCII code of the characters
print("The list after sorting is -> \t", car_brands_mixed_case)
# ['Audi', 'Ford', 'Hyundai', 'Kia', 'Mercedes-Benz', 'Nissan', 'Porsche', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo', 'alfa-Romeo', 'bMW', 'chevrolet', 'honda', 'lexus']

# how to sort case-insensitively
car_brands_mixed_case.sort(key=str.lower)
print("The list after sorting is -> \t", car_brands_mixed_case)

# how to sort case-insensitively in reverse mode
car_brands_mixed_case.sort(key=str.lower, reverse=True)
print("The list after sorting is -> \t", car_brands_mixed_case)
