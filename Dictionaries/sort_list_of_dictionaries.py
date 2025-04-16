# as there is no predefined possibility of sorting dictionaries, one has to import the module operator

from operator import itemgetter # import only the function itemgetter() from the operator module, and not the others to spare memory

aro_models = [
    {
        "model": "ARO M461",
        "production_years": "1964–1975",
        "body_type": "4x4 Off-road Vehicle",
        "engine": "2.5L M207 petrol, 70 hp",
        "notable_features": "Successor to the M59; improved mechanics; widely exported"
    },
    {
        "model": "ARO 240",
        "production_years": "1972–2006",
        "body_type": "2-door Convertible SUV",
        "engine": "Various petrol and diesel engines ranging from 2.5L to 3.1L",
        "notable_features": "First model of the ARO 24 series; versatile off-road capabilities"
    },
    {
        "model": "ARO 244",
        "production_years": "1972–2006",
        "body_type": "4-door SUV",
        "engine": "Various petrol and diesel engines; later models included Toyota engines",
        "notable_features": "Most popular ARO model; exported globally; known for durability"
    },
    {
        "model": "ARO 10",
        "production_years": "1980–2006",
        "body_type": "Compact SUV",
        "engine": "1.3L Dacia petrol; later models included Renault and Peugeot diesel engines",
        "notable_features": "Smaller and more affordable; marketed abroad as Dacia Duster"
    },
    {
        "model": "ARO Spartana",
        "production_years": "1997–2006",
        "body_type": "Open-top SUV",
        "engine": "1.6L petrol, 105 hp; 1.9L diesel, 93 hp",
        "notable_features": "Lightweight recreational vehicle; modernized design"
    },
    {
        "model": "ARO 320",
        "production_years": "1975–2006",
        "body_type": "2-door Pickup",
        "engine": "Various engines from the ARO 24 series",
        "notable_features": "Extended chassis; used for cargo and utility purposes"
    },
    {
        "model": "ARO Dragon",
        "production_years": "1997–2006",
        "body_type": "Military Vehicle",
        "engine": "Various diesel engines",
        "notable_features": "Armored military variant; used by Romanian armed forces"
    }
]

print("The list of dictionaries is \t ->", aro_models)


print("\n\nsort by model ascending (default) \n ->", sorted(aro_models,key=itemgetter("model")))

print("\n\nsort by model descending \n ->", sorted(aro_models,key=itemgetter("model"),reverse=True))

print("\n\nsort by body-type ascending (default) \n ->", sorted(aro_models,key=itemgetter("body_type")))
print("\n\nsort by body-type descending \n ->", sorted(aro_models,key=itemgetter("body_type"),reverse=True))