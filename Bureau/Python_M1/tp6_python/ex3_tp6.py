def readfile(fichier):
   
    try:
        with open("fichierrr.txt", "r") as fichier: 
            contenu = fichier.read()
            
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' n'existe pas.")
        return None
    
try:
  contenu=readfile("fichierrr.txt")
  if contenu:
               print("Contenu du fichier :")
               print(contenu)    
except
