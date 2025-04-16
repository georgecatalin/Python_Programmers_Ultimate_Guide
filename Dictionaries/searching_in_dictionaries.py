cable_specs = {
    "TXL-18AWG": {
        "Voltage Rating": "600V",
        "Temperature Rating": "-40°C to 125°C",
        "Color": "Red",
        "Application": "Automotive low-voltage circuits"
    },
    "GXL-16AWG": {
        "Voltage Rating": "60V",
        "Temperature Rating": "-40°C to 125°C",
        "Color": "Black",
        "Application": "Under-hood automotive wiring"
    },
    "FLRY-B-0.5mm²": {
        "Voltage Rating": "60V",
        "Temperature Rating": "-40°C to 105°C",
        "Color": "Blue",
        "Application": "European vehicle wiring"
    }
}

# we can use 'in' and 'not in'  for seaching in dictionary objects

# searching into keys (by default with the 'in' operator)
print("GXL-16AWG" in cable_specs) # True
print("GXL-16AWGFF" in cable_specs) # False
print("FLRY-B-0.5mm²" not in cable_specs) # False
print("FLRYyy-B-0.5mm²" not in cable_specs) # True



simple_dictionary = {"name":"George","age":46,"gender":"Male"}
# searching into values
print("George" in simple_dictionary.values()) # True
print("Mara" in simple_dictionary.values()) # False

print("Sorina" not in simple_dictionary.values()) # True

