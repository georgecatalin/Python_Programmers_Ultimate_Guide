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

print("Initial list -> \t", car_brands)

# overwrite a single element in a list
car_brands[1] = "Dacia"
print("After change this is the new list -> \t", car_brands)

# overwrite multiple elements in a list -> overwrite less elements than initially
car_brands[2:5] = ["Lada", "Renault"]
# ['Toyota', 'Dacia', "Lada", "Renault" , 'Volkswagen', 'Audi', 'Chevrolet', 'Hyundai', 'Nissan', 'Kia', 'Lexus', 'Volvo', 'Porsche', 'Tesla']
print("After change this is the new list -> \t", car_brands)

# overwrite multiple elements in a list -> overwrite more elements than initially
car_brands[2:5] = ["car brand", "car brand", "car brand", "car brand", "car brand"]
# ['Toyota', 'Dacia', "car brand", "car brand", "car brand", "car brand", "car brand" , 'Audi', 'Chevrolet', 'Hyundai', 'Nissan', 'Kia', 'Lexus', 'Volvo', 'Porsche', 'Tesla']
print("After change this is the new list -> \t", car_brands)

# overwrite multiple elements in a list -> overwrite a single element instead of many
car_brands[2:5] = ["this car brand"]
# ['Toyota', 'Dacia', 'this car brand', "car brand", "car brand" , 'Audi', 'Chevrolet', 'Hyundai', 'Nissan', 'Kia', 'Lexus', 'Volvo', 'Porsche', 'Tesla']
print("After change this is the new list -> \t", car_brands)

# append a single element at the end of the list
car_brands.append("Mahindra")
print("After change this is the new list -> \t", car_brands)

# append a single element at the end of the list as a nested list
car_brands.append(["Nio", "Byd"])
print("After change this is the new list -> \t", car_brands)

# insert a single element at a given position
car_brands.insert(1,"Xiaomi")
# ['Toyota', 'Xiaomi', 'Dacia', 'this car brand', 'car brand', 'car brand', 'Audi', 'Chevrolet', 'Hyundai', 'Nissan', 'Kia', 'Lexus', 'Volvo', 'Porsche', 'Tesla', 'Mahindra', ['Nio', 'Byd']]
print("After change this is the new list -> \t", car_brands)

# insert a single element at a given position as a nested list
car_brands.insert(1,["Xiaomi","Byd"])
print("After change this is the new list -> \t", car_brands)

# insert multiple elements at a given position as sepaate elements
car_brands[1:1] = ["Xiaomi","Byd"]
print("After change this is the new list -> \t", car_brands)

# append multiple elements at the end of the list
car_brands.extend(["car brand1", "car brand2"])
print("After change this is the new list -> \t", car_brands)

# append multiple elements at the end of the list with concatenation not memory efficient as it creates a new object for car_brands list while releasing the old object in the pool to the garbage collector
car_brands = car_brands + ["car brand3", "car brand4"]
print("After change this is the new list -> \t", car_brands)

# append multiple elements with the splat (*) operator
car_brands = [*car_brands, "car brand5", "car brand6"]
print("After change this is the new list -> \t", car_brands)

# append multiple elements with the splat (*) operator in any desired position
car_brands = ["car brand 7", *car_brands, "car brand8"]
print("After change this is the new list -> \t", car_brands)
