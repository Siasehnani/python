with open("/home/assia/phrases.txt","w") as fichier:
    for i in range(0,3):
        phrase=str(input('Entrer une phrase  \n'))
        fichier.write(phrase + "\n")