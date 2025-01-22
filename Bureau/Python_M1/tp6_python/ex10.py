def log_error(message):
    
    import logging
    logging.basicConfig(
        filename="error.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.error(message)

def read_file(filename):
   
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        error_message = f"Erreur : le fichier '{filename}' n'a pas été trouvé."
        log_error(error_message)
        raise FileNotFoundError(error_message)

def get_positive_integer():
    
    while True:
        try:
            user_input = input("Veuillez saisir un entier positif : ")
            value = int(user_input)
            if value <= 0:
                raise ValueError("Le nombre doit être strictement positif.")
            return value
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

def main():

    # Étape 1 : Lecture du fichier
    while True:
        try:
            filename = input("Veuillez entrer le nom du fichier à lire : ")
            file_content = read_file(filename)
            print("\nContenu du fichier :")
            print(file_content)
            break
        except FileNotFoundError as e:
            print(e)
            print("Veuillez réessayer avec un fichier valide.")

    # Étape 2 : Saisie d'un entier positif
    positive_integer = get_positive_integer()
    print(f"\nVous avez saisi l'entier positif : {positive_integer}")

    print("\n=== Fin du programme ===")

# Exécution du programme
if __name__ == "__main__":
    main()
