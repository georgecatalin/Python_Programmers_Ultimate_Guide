german_ww2_aircraft = [
    {
        "Aircraft": "Messerschmitt Bf 109",
        "Year": 1937,
        "Role": "Fighter",
        "Manufacturer": "Messerschmitt",
        "Engine": "Daimler-Benz DB 605A-1 V12",
        "Max Speed": "640 km/h"
    },
    {
        "Aircraft": "Messerschmitt Bf 110",
        "Year": 1937,
        "Role": "Heavy Fighter / Night Fighter",
        "Manufacturer": "Messerschmitt",
        "Engine": "2 × Daimler-Benz DB 601 V12",
        "Max Speed": "560 km/h"
    },
    {
        "Aircraft": "Messerschmitt Me 262",
        "Year": 1944,
        "Role": "Jet Fighter",
        "Manufacturer": "Messerschmitt",
        "Engine": "2 × Junkers Jumo 004B turbojets",
        "Max Speed": "870 km/h"
    },
    {
        "Aircraft": "Focke-Wulf Fw 190",
        "Year": 1941,
        "Role": "Fighter / Ground Attack",
        "Manufacturer": "Focke-Wulf",
        "Engine": "BMW 801 radial engine",
        "Max Speed": "656 km/h"
    },
    {
        "Aircraft": "Focke-Wulf Ta 152",
        "Year": 1945,
        "Role": "High-Altitude Interceptor",
        "Manufacturer": "Focke-Wulf",
        "Engine": "Junkers Jumo 213E V12",
        "Max Speed": "755 km/h"
    },
    {
        "Aircraft": "Heinkel He 111",
        "Year": 1937,
        "Role": "Medium Bomber",
        "Manufacturer": "Heinkel",
        "Engine": "2 × Junkers Jumo 211F-2 V12",
        "Max Speed": "440 km/h"
    },
    {
        "Aircraft": "Heinkel He 162",
        "Year": 1945,
        "Role": "Jet Fighter",
        "Manufacturer": "Heinkel",
        "Engine": "BMW 003E-1 turbojet",
        "Max Speed": "905 km/h"
    },
    {
        "Aircraft": "Heinkel He 219",
        "Year": 1943,
        "Role": "Night Fighter",
        "Manufacturer": "Heinkel",
        "Engine": "2 × Daimler-Benz DB 603A V12",
        "Max Speed": "616 km/h"
    },
    {
        "Aircraft": "Junkers Ju 87",
        "Year": 1936,
        "Role": "Dive Bomber",
        "Manufacturer": "Junkers",
        "Engine": "Junkers Jumo 211D V12",
        "Max Speed": "410 km/h"
    },
    {
        "Aircraft": "Junkers Ju 88",
        "Year": 1939,
        "Role": "Bomber / Night Fighter",
        "Manufacturer": "Junkers",
        "Engine": "2 × Junkers Jumo 211 V12",
        "Max Speed": "470 km/h"
    },
    {
        "Aircraft": "Junkers Ju 188",
        "Year": 1943,
        "Role": "Bomber / Reconnaissance",
        "Manufacturer": "Junkers",
        "Engine": "2 × BMW 801 radial engines",
        "Max Speed": "550 km/h"
    },
    {
        "Aircraft": "Junkers Ju 290",
        "Year": 1943,
        "Role": "Long-Range Reconnaissance / Transport",
        "Manufacturer": "Junkers",
        "Engine": "4 × BMW 801D radial engines",
        "Max Speed": "440 km/h"
    },
    {
        "Aircraft": "Arado Ar 234",
        "Year": 1944,
        "Role": "Jet Bomber / Reconnaissance",
        "Manufacturer": "Arado",
        "Engine": "2 × Junkers Jumo 004B turbojets",
        "Max Speed": "742 km/h"
    },
    {
        "Aircraft": "Dornier Do 17",
        "Year": 1937,
        "Role": "Light Bomber / Reconnaissance",
        "Manufacturer": "Dornier",
        "Engine": "2 × Bramo 323 radial engines",
        "Max Speed": "410 km/h"
    },
    {
        "Aircraft": "Dornier Do 217",
        "Year": 1941,
        "Role": "Medium Bomber / Night Fighter",
        "Manufacturer": "Dornier",
        "Engine": "2 × BMW 801 radial engines",
        "Max Speed": "515 km/h"
    },
    {
        "Aircraft": "Dornier Do 335",
        "Year": 1944,
        "Role": "Heavy Fighter / Bomber",
        "Manufacturer": "Dornier",
        "Engine": "2 × Daimler-Benz DB 603 V12",
        "Max Speed": "765 km/h"
    },
    {
        "Aircraft": "Henschel Hs 129",
        "Year": 1942,
        "Role": "Ground Attack",
        "Manufacturer": "Henschel",
        "Engine": "2 × Gnome-Rhône 14M radial engines",
        "Max Speed": "407 km/h"
    },
    {
        "Aircraft": "Blohm & Voss BV 138",
        "Year": 1940,
        "Role": "Maritime Patrol / Reconnaissance",
        "Manufacturer": "Blohm & Voss",
        "Engine": "3 × Junkers Jumo 205D diesel engines",
        "Max Speed": "285 km/h"
    },
    {
        "Aircraft": "Blohm & Voss BV 222",
        "Year": 1942,
        "Role": "Transport Flying Boat",
        "Manufacturer": "Blohm & Voss",
        "Engine": "6 × BMW 801 radial engines",
        "Max Speed": "390 km/h"
    },
    {
        "Aircraft": "Fieseler Fi 156 Storch",
        "Year": 1937,
        "Role": "Liaison / Reconnaissance",
        "Manufacturer": "Fieseler",
        "Engine": "Argus As 10C V8",
        "Max Speed": "175 km/h"
    }
]

print("Here is the list of dictionaries we're playing with: \t -> \n", german_ww2_aircraft)

for i in german_ww2_aircraft:
    print(i) # prints out each dictionary
    for j in i:
        print("\t\tKey =",j,"\tvalue =",i[j])