class Forme:
    def calculer_surface(self):
        raise NotImplementedError("Cette méthode doit être implémentée dans une classe dérivée.")
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_surface(self):
        from math import pi
        return pi * (self.rayon ** 2)
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def calculer_surface(self):
        return self.largeur * self.hauteur

