opel_models_1985_2020 = [
    "Opel Corsa A",         # 1982–1993
    "Opel Corsa B",         # 1993–2000
    "Opel Corsa C",         # 2000–2006
    "Opel Corsa D",         # 2006–2014
    "Opel Corsa E",         # 2014–2019
    "Opel Astra F",         # 1991–1998
    "Opel Astra G",         # 1998–2004
    "Opel Astra H",         # 2004–2009
    "Opel Astra J",         # 2009–2015
    "Opel Astra K",         # 2015–2021
    "Opel Vectra A",        # 1988–1995
    "Opel Vectra B",        # 1995–2002
    "Opel Vectra C",        # 2002–2008
    "Opel Omega A",         # 1986–1994
    "Opel Omega B",         # 1994–2003
    "Opel Kadett E",        # 1984–1993
    "Opel Calibra",         # 1989–1997
    "Opel Tigra A",         # 1994–2001
    "Opel Tigra B",         # 2004–2009
    "Opel Meriva A",        # 2003–2010
    "Opel Meriva B",        # 2010–2017
    "Opel Zafira A",        # 1999–2005
    "Opel Zafira B",        # 2005–2014
    "Opel Zafira Tourer C", # 2011–2019
    "Opel Insignia A",      # 2008–2017
    "Opel Insignia B",      # 2017–2020
    "Opel Signum",          # 2003–2008
    "Opel Agila A",         # 2000–2007
    "Opel Agila B",         # 2008–2014
    "Opel Adam",            # 2013–2019
    "Opel Ampera",          # 2011–2015
    "Opel Cascada",         # 2013–2018
    "Opel Mokka",           # 2012–2019
    "Opel Antara",          # 2006–2015
    "Opel Frontera A",      # 1991–1998
    "Opel Frontera B",      # 1998–2004
    "Opel Combo B",         # 1993–2001
    "Opel Combo C",         # 2001–2011
    "Opel Combo D",         # 2011–2018
    "Opel Combo E",         # 2018–2020
    "Opel Crossland X",     # 2017–2020
    "Opel Grandland X",     # 2017–2020
    "Opel Manta B",         # 1975–1988
    "Opel Senator B",       # 1987–1993
    "Opel Monza",           # 1978–1986
    "Opel Rekord E",        # 1977–1986
    "Opel Ascona C",        # 1981–1988
    "Opel Kadett D",        # 1979–1984
    "Opel Kadett E",        # 1984–1993
    "Opel Karl",            # 2015–2019
]

print("The initial list is -> \t", opel_models_1985_2020)

# one can copy the list, either by copying the address of the list object it is pointing to in the Object Pool of the  Arena,
# or by creating a completely copy of the initial list object

# copy by reference

opel_models_copied_by_reference = opel_models_1985_2020
opel_models_copied_by_reference.append("This extra Opel") # add a new object in the initial list to check if the list change is visibile in both

print("The initial list is -> \t", opel_models_1985_2020)
print("The list copied by reference is -> \t", opel_models_1985_2020)



vw_models_1985_2020 = [
    "Volkswagen Golf Mk2",       # 1983–1992
    "Volkswagen Golf Mk3",       # 1991–1997
    "Volkswagen Golf Mk4",       # 1997–2003
    "Volkswagen Golf Mk5",       # 2003–2009
    "Volkswagen Golf Mk6",       # 2008–2012
    "Volkswagen Golf Mk7",       # 2012–2019
    "Volkswagen Golf Mk8",       # 2019–present
    "Volkswagen Jetta Mk2",      # 1984–1992
    "Volkswagen Vento",          # 1992–1999
    "Volkswagen Bora",           # 1999–2005
    "Volkswagen Jetta Mk5",      # 2005–2010
    "Volkswagen Jetta Mk6",      # 2010–2018
    "Volkswagen Jetta Mk7",      # 2018–present
    "Volkswagen Passat B2",      # 1981–1988
    "Volkswagen Passat B3",      # 1988–1993
    "Volkswagen Passat B4",      # 1993–1997
    "Volkswagen Passat B5",      # 1996–2005
    "Volkswagen Passat B6",      # 2005–2010
    "Volkswagen Passat B7",      # 2010–2015
    "Volkswagen Passat B8",      # 2015–present
    "Volkswagen Polo Mk2",       # 1981–1994
    "Volkswagen Polo Mk3",       # 1994–2002
    "Volkswagen Polo Mk4",       # 2002–2009
    "Volkswagen Polo Mk5",       # 2009–2017
    "Volkswagen Polo Mk6",       # 2017–present
    "Volkswagen Scirocco Mk2",   # 1981–1992
    "Volkswagen Scirocco Mk3",   # 2008–2017
    "Volkswagen Corrado",        # 1988–1995
    "Volkswagen Lupo",           # 1998–2005
    "Volkswagen Fox",            # 2005–2011
    "Volkswagen Up!",            # 2011–present
    "Volkswagen Sharan Mk1",     # 1995–2010
    "Volkswagen Sharan Mk2",     # 2010–2022
    "Volkswagen Touran",         # 2003–present
    "Volkswagen Tiguan",         # 2007–present
    "Volkswagen Touareg",        # 2002–present
    "Volkswagen T-Roc",          # 2017–present
    "Volkswagen T-Cross",        # 2018–present
    "Volkswagen Arteon",         # 2017–present
    "Volkswagen Phaeton",        # 2002–2016
    "Volkswagen New Beetle",     # 1997–2011
    "Volkswagen Beetle (A5)",    # 2011–2019
    "Volkswagen Passat CC",      # 2008–2012
    "Volkswagen CC",             # 2012–2017
    "Volkswagen Eos",            # 2006–2015
    "Volkswagen Caddy Mk2",      # 1995–2003
    "Volkswagen Caddy Mk3",      # 2003–2015
    "Volkswagen Caddy Mk4",      # 2015–2020
    "Volkswagen Transporter T3", # 1979–1992
    "Volkswagen Transporter T4", # 1990–2003
    "Volkswagen Transporter T5", # 2003–2015
    "Volkswagen Transporter T6", # 2015–2019
    "Volkswagen Transporter T6.1", # 2019–present
]

print("The initial list is -> \t", vw_models_1985_2020)
vw_models_1985_2020_copied_value = vw_models_1985_2020.copy()

# add a new element to the initial list
vw_models_1985_2020.append("NEW VW")
print("The initial list is -> \t", vw_models_1985_2020)
print("The new list copied by value is -> \t", vw_models_1985_2020_copied_value)

new_list = [1978, 1954, 1953] * 10 # list multiplicator
print("This is a list constructed with the multiplicator \t ->" , new_list)
