with open('/home/assia/fichier.txt') as fichier:
    lignes=fichier.readlines()
    x=1
    for ligne in lignes:
        print(x,":",ligne.strip())
        x+=1
