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

print("The dictionary object printed : \t ->", bf109g6_specs)

# for loop for the keys
for i in bf109g6_specs:
    print(i," \t : \t", bf109g6_specs[i])

# for loop for the values, without the need of keys
print(bf109g6_specs.values())
for i in bf109g6_specs.values():
    print("Value= \t",i)

# for loop with items() which creates a list of tuples (key,value)
print(bf109g6_specs.items())
for i in bf109g6_specs.items():
    print(i, i[0], i[1]) # i[0] is the first element of the tuple, i[1] the second

# for loop with items() which creates a list of tuples (key,value), but unpacking the tuple
print(bf109g6_specs.items())
for (var_a,var_b) in bf109g6_specs.items():
    print(var_a," \t : \t ", var_b)