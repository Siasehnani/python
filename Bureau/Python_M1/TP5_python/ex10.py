import csv

# Fonction pour ajouter un contact au fichier CSV
def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    telephone = input("Entrez le numéro de téléphone du contact : ")
    email = input("Entrez l'email du contact : ")

    with open('contacts.csv', mode='a', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, telephone, email])
        print("Contact ajouté avec succès.")

# Fonction pour afficher tous les contacts
def afficher_contacts():
    try:
        with open('contacts.csv', mode='r') as fichier:
            reader = csv.reader(fichier)
            print("Liste des contacts :")
            for contact in reader:
                print(f"Nom : {contact[0]}, Téléphone : {contact[1]}, Email : {contact[2]}")
    except FileNotFoundError:
        print("Le fichier contacts.csv n'existe pas. Aucun contact à afficher.")

# Fonction pour rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Entrez le nom du contact à rechercher : ")
    try:
        with open('contacts.csv', mode='r') as fichier:
            reader = csv.reader(fichier)
            trouvé = False
            for contact in reader:
                if contact[0].lower() == nom_recherche.lower():
                    print(f"Contact trouvé - Nom : {contact[0]}, Téléphone : {contact[1]}, Email : {contact[2]}")
                    trouvé = True
                    break
            if not trouvé:
                print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier contacts.csv n'existe pas.")

# Fonction pour supprimer un contact
def supprimer_contact():
    nom_suppression = input("Entrez le nom du contact à supprimer : ")
    try:
        contacts = []
        with open('contacts.csv', mode='r') as fichier:
            reader = csv.reader(fichier)
            contacts = list(reader)
        
        with open('contacts.csv', mode='w', newline='') as fichier:
            writer = csv.writer(fichier)
            contact_supprimé = False
            for contact in contacts:
                if contact[0].lower() == nom_suppression.lower():
                    print(f"Contact {contact[0]} supprimé.")
                    contact_supprimé = True
                else:
                    writer.writerow(contact)
            if not contact_supprimé:
                print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier contacts.csv n'existe pas.")

# Fonction principale
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact par nom")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            afficher_contacts()
        elif choix == '3':
            rechercher_contact()
        elif choix == '4':
            supprimer_contact()
        elif choix == '5':
            print("Merci d'avoir utilisé l'application.")
            break
        else:
            print("Choix invalide. Essayez de nouveau.")


menu()
