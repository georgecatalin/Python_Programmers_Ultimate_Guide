person = {"name":"George","age":46,"job":"Manager"}

# George is a Manager

print(f"{person["name"]} is a {person["job"]}")

print("{emp[name]} is a {emp[job]}".format(emp = person))

print("{name} is a {job}.".format_map(person))