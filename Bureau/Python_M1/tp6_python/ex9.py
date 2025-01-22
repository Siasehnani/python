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

