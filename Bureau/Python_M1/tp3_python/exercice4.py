class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if prix < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        self.__prix = prix

    def calculer_prix(self, montant, remise):
        if self.__prix > montant:
            return self.__prix * (1 - remise)
        return self.__prix

    def afficher_produit(self):
        print(f"Produit: {self.nom}, Prix: {self.prix:.2f} DH")


P1 = Produit("Pain", 2)
P2 = Produit("Lait", 4)

P1.afficher_produit()
P2.afficher_produit()
print(P1.calculer_prix(100, 10))
print(P2.calculer_prix(50, 20))

