class Employe:
    def __init__(self,nom,prenom,salaire):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
    
class Manager(Employe):
    def __init__(self,nom,prenom,salaire):
        super().__init__(nom, prenom, salaire)
        self.empls = []

    def ajout_empl(self,employe):
        if isinstance(employe, Employe):
          self.empls.append(employe)
    def afficher_empl(self):
     print(f"Manager: {self.nom} {self.prenom}")
     print("Liste des employés supervisés :")
     for index, employe in enumerate(self.empls, start=1): 
        print(f" Employe {index}: {employe.nom} {employe.prenom}")
 

E1=Employe("SEHNANI","ASSIA",9000)
E2=Employe("NMER","NOUR EL HOUDA",10000)
mng=Manager("JABRANE","AYA",12000)

mng.ajout_empl(E1)

mng.ajout_empl(E2)
mng.afficher_empl()