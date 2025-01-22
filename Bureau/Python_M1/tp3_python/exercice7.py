from abc import ABC, abstractmethod

class Vehicule(ABC):
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture roule sur la route.")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette avance en pédalant.")


v=Voiture()
B=Bicyclette()
v.deplacer()     
B.deplacer()   
