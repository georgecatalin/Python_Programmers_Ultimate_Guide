person = {"name":"George", "age":46, "gender":"male",
          "address":{"street": "name of street", "city": "name of city", "country": "name of country"},
          "phones": ["0722 764836", "0753 568417"],
          "parents": ("Sandu","Vasilica")
          }

print(f"The initial dictionary is {person}")

# get the whole nested dictionary
print(person["address"])
# get the city
print(person["address"]["city"])

# get the whole nested list
print(person["phones"])
print(person["phones"][0]) # 0722 764836

# get the whole nested tuple (immutable)
print(person["parents"])
print(person["parents"][1]) # Vasilica