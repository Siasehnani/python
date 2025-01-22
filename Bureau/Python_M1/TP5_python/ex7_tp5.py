import shutil
import os
Fichier1="journal.txt"
contenu="Ceci est un journal.\n Je m'appelle ASSIA SEHNANI."

with open(Fichier1,"w") as fichier:
    fichier.write(contenu) 
    print(f"Le fichier '{Fichier1}' a ete créer avec succés")

Fichier_copier="journal_copie.txt"
try:
    shutil.copy(Fichier1, Fichier_copier)
    print(f"Le fichier '{Fichier1}' a été copié en '{Fichier_copier}'.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la copie : {e}")

dossier_archives = "archives"

try:
    os.makedirs(dossier_archives)  # Créer le dossier s'il n'existe pas
    shutil.move(Fichier_copier, os.path.join(dossier_archives, Fichier_copier))
    print(f"Le fichier '{Fichier_copier}' a été déplacé dans le dossier '{dossier_archives}'.")
except Exception as e:
    print(f"Une erreur s'est produite lors du déplacement : {e}")
