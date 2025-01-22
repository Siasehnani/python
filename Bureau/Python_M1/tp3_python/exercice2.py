class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        self.__nom=nom
    def get_prenom(self):
        return self.__prenom
    def set_prenom(self,prenom):
        self.__prenom=prenom
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
    
P1=Personne("NMER","Houda",20)
P2=Personne("SEHNANI","Assia",23)
print(P1.get_nom(),P1.get_prenom(),P1.get_age())
print(P2.get_nom(),P2.get_prenom(),P2.get_age())
