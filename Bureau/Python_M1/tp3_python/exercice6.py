class Commande:
    def __init__(self,produit,quantité):
        self.produit=produit
        self.quantité=quantité
    
class Panier(Commande):
    def __init__(self,produit,quantité):
        super().__init__(produit,quantité)
        self.liste_cmd= []

    def ajout_commande(self,cmd):
        if isinstance(cmd, Commande):
          self.liste_cmd.append(cmd)
    def Calcul_Panier(self):
        return sum(Commande.produit.get_prix() * Commande.quantité for Commande in self.Commandes)      
