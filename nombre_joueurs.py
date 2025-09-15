# Demander le nombre de joueurs

def demander_nb_joueurs():
    while True:
        try:
            nb = int(input("Combien de joueurs (1-3)? "))
            if 1 <= nb <= 3:
                return nb
            else:
                # Affiche un message d'erreur si le nombre n'est pas entre 1 et 3
                print("Veuillez entrer un nombre entre 1 et 3.")
        except ValueError:
            # Affiche un message d'erreur si l'entrée n'est pas un entier
            print("Entrée invalide : Veuillez entrer un nombre entier.")


# Exemple pour tester la fonction

# if __name__ == "__main__" empêche l'exécution du code lors de l'importation du module dans un autre 
# fichier
if __name__ == "__main__":
    nb_joueurs = demander_nb_joueurs()
    print(f"Nombre de joueurs : {nb_joueurs}")