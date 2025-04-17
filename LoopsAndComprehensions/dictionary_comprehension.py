"""
* comprehension applied to a dictionary creates a new dictionary collection
* the syntax of the dictionary comprehension is :
    key:value for variable in collection if condition
"""

bf109g6_specs = {
    "Aircraft": "Messerschmitt Bf 109G-6",
    "Crew": 1,
    "Length": "8.95 m",
    "Wingspan": "9.97 m",
    "Height": "2.60 m",
    "Wing Area": "16.4 m²",
    "Empty Weight": "2,250 kg",
    "Loaded Weight": "3,200 kg",
    "Powerplant": "1 × Daimler-Benz DB 605A-1 inverted V-12 engine",
    "Engine Power": "1,475 hp",
    "Maximum Speed": "630 km/h at 6,600 m",
    "Range": "560 km (850 km with external tank)",
    "Service Ceiling": "12,000 m",
    "Rate of Climb": "Not specified",
    "Armament": {
        "Nose-mounted": "1 × 20 mm MG 151/20 cannon (200 rounds)",
        "Cowling-mounted": "2 × 13 mm MG 131 machine guns (300 rounds each)",
        "Optional": "Underwing gun pods or bombs"
    }
}

print(f"This is the dictionary \t : \n {bf109g6_specs}")

# no expression, no filtering
print("no expression, no filtering")
print({ i:bf109g6_specs[i] for i in bf109g6_specs})

# an expression, without filtering
print("an expression, without filtering")
print({ i:str(bf109g6_specs[i]).swapcase() for i in bf109g6_specs})

# an expression with filtering
print("an expression with filtering")
print({i:str(bf109g6_specs[i]).upper()  for i in bf109g6_specs if i !="Powerplant"})