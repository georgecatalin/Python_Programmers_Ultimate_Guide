# exceptions avoid applications to crash, and instead they allow graceful resolution of unwanted situations

nato_fighter_aircraft_2025 = [
    "F-35 Lightning II",            # USA, UK, Italy, Netherlands, Norway, Denmark, Belgium, Poland, Finland, Canada
    "F-22 Raptor",                  # USA
    "F-15 Eagle",                   # USA
    "F-15EX Eagle II",             # USA (newer variant being adopted)
    "F-16 Fighting Falcon",        # USA, Belgium, Denmark, Netherlands, Norway, Greece, Turkey, Poland, Portugal, Romania, Bulgaria, Slovakia
    "F/A-18 Hornet",               # Spain (Navy), Canada (older variant)
    "F/A-18E/F Super Hornet",      # USA (Navy), Australia (not NATO), Germany (planned for nuclear role)
    "Eurofighter Typhoon",         # UK, Germany, Italy, Spain
    "Dassault Rafale",             # France, Greece, Croatia
    "Saab JAS 39 Gripen",          # Czech Republic, Hungary
    "AV-8B Harrier II",            # Italy (Navy), Spain (Navy)
    "McDonnell Douglas F-4 Phantom II",  # Turkey (being retired), Greece (retired)
    "Northrop F-5 Tiger II",       # Greece (limited), Turkey (training), Spain (retired)
    "MiG-29 Fulcrum",              # Poland, Slovakia (being phased out), Bulgaria (still in limited use)
    "MiG-21 Fishbed",              # Romania, Croatia (phasing out)
    "Panavia Tornado",             # Germany, Italy, UK (retired)
    "Mirage 2000",                 # France, Greece
    "Mirage F1",                   # Greece (retired), France (retired)
    "SEPECAT Jaguar",             # France (retired, but recently in storage/testing)
    "Su-22 Fitter",                # Poland (being retired)
]

try:
    print(nato_fighter_aircraft_2025[1]) # F-22 Raptor
    print(len(nato_fighter_aircraft_2025)) # 20
    print(nato_fighter_aircraft_2025[20]) # IndexError: list index out of range, gotta deal with this via try: except: finally:
except IndexError:
    print("You have provided an index out of range")
finally:
    print("Application terminated here")

"""
F-22 Raptor
20
You have provided an index out of range
Application terminated here

"""