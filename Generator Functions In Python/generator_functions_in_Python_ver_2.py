# generator functions represent a special type of functions that run-and-pause or return-and-pause

car_brands = [
    "Toyota",         # Japan
    "Honda",          # Japan
    "Ford",           # USA
    "Chevrolet",      # USA
    "Volkswagen",     # Germany
    "BMW",            # Germany
    "Mercedes-Benz",  # Germany
    "Audi",           # Germany
    "Porsche",        # Germany
    "Fiat",           # Italy
    "Ferrari",        # Italy
    "Lamborghini",    # Italy
    "Alfa Romeo",     # Italy
    "Peugeot",        # France
    "Renault",        # France
    "Citroën",        # France
    "Hyundai",        # South Korea
    "Kia",            # South Korea
    "Genesis",        # South Korea
    "Tata Motors",    # India
    "Mahindra",       # India
    "Volvo",          # Sweden
    "Saab",           # Sweden (historical)
    "Skoda",          # Czech Republic
    "SEAT",           # Spain
    "Tesla",          # USA
    "Lucid Motors",   # USA
    "BYD",            # China
    "Geely",          # China
    "Holden"          # Australia (historical)
]


# we wish to print several chunks of the list of car brands as it follows
#  1st time : 10 brands
#  2nd time : 5 brands
#  3rd time : 7 brands
# 4th time : the rest of the car brands from the list

def generator_function():
    current_index_in_the_list = 0
    yield car_brands[current_index_in_the_list:current_index_in_the_list + 10]
    current_index_in_the_list += 10
    yield car_brands[current_index_in_the_list:current_index_in_the_list + 5]
    current_index_in_the_list += 5
    yield car_brands[current_index_in_the_list:current_index_in_the_list + 7]
    current_index_in_the_list += 7
    yield  car_brands[current_index_in_the_list:]

generator_object_reference_variable = generator_function()
print("Reference variable for the generator object that was created in the pool of the heap(arena)", generator_object_reference_variable)

# at this moment , only the generator object was created, the function was not executed
print(next(generator_object_reference_variable)) # returns the first sequence of 10 elements of the list  and executes up to the first yield statement
print(next(generator_object_reference_variable)) # returns the second sequence with 5 elements and executes up to the second yield statement
print(next(generator_object_reference_variable)) # returns the third sequence with 7 elements  and executes upt to the third yield statement
print(next(generator_object_reference_variable)) # return the forth sequence with all remaining elements and executes up to that yield

