su35_features = (
    "Single-seat, twin-engine multirole fighter",
    "Developed from the Su-27 airframe",
    "Equipped with N035 Irbis-E PESA radar capable of detecting targets up to 400 km",
    "Powered by two Saturn AL-41F1S thrust-vectoring turbofan engines",
    "Supermaneuverability with thrust-vectoring nozzles",
    "Maximum speed of Mach 2.25",
    "Operational range of approximately 3,600 km",
    "Service ceiling around 18,000 meters",
    "12 hardpoints for various air-to-air and air-to-ground weapons",
    "Advanced avionics with digital fly-by-wire control system",
    "Glass cockpit featuring multi-function LCD displays",
    "Incorporates radar-absorbent materials to reduce radar cross-section",
    "Equipped with L175M Khibiny-M electronic countermeasure system",
    "Enhanced fuel capacity for extended range",
    "Capable of in-flight refueling",
    "Designed for both air superiority and ground attack missions"
)

print("The tuple is \t ->", su35_features)

# loop with the iterator tuple
for i in su35_features:
    print("element of the tuple is: \t ->", i)
    
# loop with the range iterator
for i in range(0,len(su35_features)):
    print(i, su35_features[i])

# loop with enumerate() function into tuple (index, collection[index])
for i in enumerate(su35_features):
    print(i,i[0],i[1])
