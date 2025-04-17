russian_fighter_aircraft = [
    # MiG Series
    "MiG-19",
    "MiG-21",
    "MiG-23",
    "MiG-25",
    "MiG-27",
    "MiG-29",
    "MiG-31",
    "MiG-35",

    # Sukhoi (Su) Series
    "Su-7",
    "Su-9",
    "Su-11",
    "Su-15",
    "Su-17",
    "Su-24",
    "Su-25",
    "Su-27",
    "Su-30",
    "Su-33",
    "Su-34",
    "Su-35",
    "Su-57"
]

print("The list is \t ->", russian_fighter_aircraft)

# print each element of the list
for i in russian_fighter_aircraft:
    print("Aircraft name: ", i)
print("The loop variable freezes at the last value: ", i)

# print each element of the list by means of index
for i in range(len(russian_fighter_aircraft)): # i goes from 0 .. len-1
    print("Aircraft name: ",i," -> ", russian_fighter_aircraft[i])

# print specific elements of the list
for i in [1, 3, 15]:
    print("Specific element of the list \t ",i, " -> ", russian_fighter_aircraft[i])

# extract into tuples (index, list[index]) and act upon elements with certain index
for i in enumerate(russian_fighter_aircraft):
    print(i," <> ", i[0], " <> ", i[1])

for i in enumerate(russian_fighter_aircraft):
    if i[0] == 3:
        continue
    print(i, " <> ", i[0], " <> ", i[1])