import os

ancien_nom = "phrases.txt"
nv_nom = "anciennes_phrases.txt"

try:
    os.rename(ancien_nom, nv_nom)
    print(f"Le fichier '{ancien_nom}' a été renommé en '{nv_nom}'.")
except FileNotFoundError:
    print(f"Le fichier '{ancien_nom}' n'existe pas.")
except PermissionError:
    print("Permission refusée pour renommer le fichier.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

try:
    os.remove(nv_nom)
    print(f"Le fichier '{nv_nom}' a été supprimé.")
except FileNotFoundError:
    print(f"Le fichier '{nv_nom}' n'existe pas.")
except PermissionError:
    print("Permission refusée pour supprimer le fichier.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
