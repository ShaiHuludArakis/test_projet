import json

chemin = "/users/aurelien/test_projet/fichier.json"

with open(chemin,"w") as f:
    #dump permet d'écrire dans le fichier
    json.dump(list(range(11)), f, indent=4)
with open(chemin,"r") as f:
    #load permet de lire le fichier
    list = json.load(f)
    print(list)