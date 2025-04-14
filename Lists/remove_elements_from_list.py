fighter_jets = [
    "F-22 Raptor",
    "F-35 Lightning II",
    "F-16 Fighting Falcon",
    "F/A-18 Super Hornet",
    "F-15 Eagle",
    "Eurofighter Typhoon",
    "Dassault Rafale",
    "Saab JAS 39 Gripen",
    "MiG-29 Fulcrum",
    "MiG-35",
    "Su-27 Flanker",
    "Su-30MKI",
    "Su-35S",
    "Su-57 Felon",
    "Chengdu J-10",
    "Chengdu J-20 Mighty Dragon",
    "Shenyang J-11",
    "Shenyang FC-31 Gyrfalcon",
    "HAL Tejas",
    "KF-21 Boramae"
]

print("the initial list is -> \t", fighter_jets)
#  ['F-22 Raptor', 'F-35 Lightning II', 'F-16 Fighting Falcon', 'F/A-18 Super Hornet', 'F-15 Eagle', 'Eurofighter Typhoon', 'Dassault Rafale', 'Saab JAS 39 Gripen', 'MiG-29 Fulcrum', 'MiG-35', 'Su-27 Flanker', 'Su-30MKI', 'Su-35S', 'Su-57 Felon', 'Chengdu J-10', 'Chengdu J-20 Mighty Dragon', 'Shenyang J-11', 'Shenyang FC-31 Gyrfalcon', 'HAL Tejas', 'KF-21 Boramae']

# remove a single element from the list
fighter_jets.remove("MiG-35")
print("the new list is -> \t", fighter_jets)
# ['F-22 Raptor', 'F-35 Lightning II', 'F-16 Fighting Falcon', 'F/A-18 Super Hornet', 'F-15 Eagle', 'Eurofighter Typhoon', 'Dassault Rafale', 'Saab JAS 39 Gripen', 'MiG-29 Fulcrum', 'Su-27 Flanker', 'Su-30MKI', 'Su-35S', 'Su-57 Felon', 'Chengdu J-10', 'Chengdu J-20 Mighty Dragon', 'Shenyang J-11', 'Shenyang FC-31 Gyrfalcon', 'HAL Tejas', 'KF-21 Boramae']

# remove an element (item or object) by its index
removed_element= fighter_jets.pop(1) # 'F-35 Lightning II'
print("The removed element is -> \t", removed_element)
print("the new list is -> \t", fighter_jets)

# remove the last element from the list and return it into a variable
removed_last_element = fighter_jets.pop()
print("The removed element is -> \t", removed_last_element)
print("the new list is -> \t", fighter_jets)

# remove several elements from the list by their index
del fighter_jets[1:4] # 'F-16 Fighting Falcon', 'F/A-18 Super Hornet', 'F-15 Eagle' will be removed
print("the new list is -> \t", fighter_jets)

# remove a single element from the list by its index (other variant)
del fighter_jets[1] # 'Eurofighter Typhoon' will be removed
print("the new list is -> \t", fighter_jets)

# clear the whole list of the containing list objects
fighter_jets.clear()
print("Number of elements in list :", len(fighter_jets))

# dispose the list object
del fighter_jets
