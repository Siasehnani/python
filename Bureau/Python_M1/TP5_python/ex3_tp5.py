A = input("Souhaitez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
while A=="oui":
    with open ("/home/assia/phrases.txt","a")as fichier:
        phrase=str(input('ajouter ca : \n'))
        fichier.write(phrase + "\n")
        A = input("Souhaitez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
print("Toutes les phrases ont été enregistrées.")