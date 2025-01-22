class Vehicule:
    def __init__(self,marque,model,annee):
        self.marque=marque
        self.model=model
        self.annee=annee
    def afficher_info(self):
        print(f"la marque de vehicule est:{self.marque}")
        print(f"le model de vehicule est:{self.model}")
        print(f"Annee de vehicule est:{self.annee}")

class Moteur:
    def __init__(self,puissance,typeMot):
        self.puissance=puissance
        self.typeMot=typeMot
    def afficher_moteur(self):
        print(f"Puissance de Moteur est:{self.puissance}")
        print(f"Le type de Moteur est:{self.typeMot}")
class Voiture(Vehicule,Moteur):
    def __init__(self,marque,model,annee,puissance,typeMot,nbPlace):
     Vehicule.__init__(self,marque,model,annee)
     Moteur.__init__(self,puissance,typeMot)
     self.nbPlace=nbPlace
    def afficher_info(self):
        return super().afficher_info()
class Moto(Vehicule,Moteur):
    def __init__(self,marque,model,annee,puissance,typeMot,tM):
     Vehicule.__init__(self,marque,model,annee)
     Moteur.__init__(self,puissance,typeMot)
     self.tM=tM
    def afficher_info(self):
        return super().afficher_info()

V1 = Voiture(marque="Toyota", model="Corolla", annee=2021, puissance=150, typeMot="Essence", nbPlace=5)
V1.afficher_info()          
V1.afficher_moteur()        
print(f"Nombre de places : {V1.nbPlace}")  
print("-----------------------------------------------------")
M1 = Moto(marque="Yamaha", model="R1", annee=2020, puissance=200, typeMot="Essence", tM="Sport")
M1.afficher_info()          
M1.afficher_moteur()       
print(f"Type de moto : {M1.tM}")  

