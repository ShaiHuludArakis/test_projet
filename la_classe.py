#création de la classe
class Voiture:
    #attribut de classe
    #marque = "Lamborghini"
    
    #Méthode
    def __init__(self, marque):
        #attribut d'instance
        self.marque = marque

    def afficher_marque(self):
        print(f"La marque de la voiture commence par un {self.marque}")
#instance
voiture_01=Voiture("L")
voiture_01.afficher_marque()
#plus court que d'écrire :
Voiture.afficher_marque(voiture_01)


from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

patrick = User(first_name="Patrick", last_name="Smith")
print(repr(patrick))
print(patrick.full_name)