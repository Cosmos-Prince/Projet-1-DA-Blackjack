import tkinter as tk
from Acteurs import *
from Cartes import *
from fonctions import *
from TurnOrder import *


pg = None  # Sera passé dynamiquement par le frontend

##################################################################################################



#############################################################################################################
# FONCTION POUR DEMANDER LE NOMBRE DE JOUEURS (1-3) --> À MODIFIER DANS TKINTER (PAS D'INPUT/PRINT)
#==================================================================================================

#def demander_nb_joueurs():
#    while True:
#        try:
#            nb = int(input("Combien de joueur (1-3)? "))
#            if 1 <= nb <= 3:
#                return nb
#            else:
#                print("Veuillez entrer un nombre entre 1 et 3.")
#        except ValueError:
#            print("Entrée invalide : Veuillez entrer un nombre entier.")



##############################################################################################################
# GESTION DU JEU (TOURS DES JOUEURS ET DU CROUPIER)
#==================================================


    # Résultats
    #print("\n*** RÉSULTATS ***")
    #score_croupier = calculer_score(croupier.main)
    #score_joueur = calculer_score(joueur.main)
    #if score_joueur > 21:
    #    verdict = "perdu (bust)"
    #elif score_croupier > 21 or score_joueur > score_croupier:
    #    verdict = "gagné"
    #elif score_joueur < score_croupier:
    #    verdict = "perdu"
    #else:
    #    verdict = "égalité (push)"
    #print(f"{joueur.nom}: {joueur.afficher_main()} --> {score_joueur} | {verdict}")

#if __name__ == "__main__":
    # Mainloop de la fenêtre Tkinter
#    gerer_les_tours()
#    pg.fenetre.mainloop()

    # Affichage de la première carte du joueur
    # print(joueur.afficher_premier_carte())  # joueur est maintenant local à gerer_les_tours





'''
ÉTAIT DANS PAGE DE JEU MAIS JSP SI NÉCESSAIRE

choix_joueur = tk.StringVar(value="")  # Variable pour stocker le choix

    
-------------------------------------------------------------- Cartes du dealer --------------------------------------------------------------#

# Outline de la 1ere carte dealer


# Outline de la 2eme carte dealer, face cachée
carte2 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
carte2.place(x=100, y=50)

# Optionnel : ajouter du texte ou un symbole sur la 2ème carte
carte2.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 3ème carte dealer, superposée
carte3 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
carte3.place(x=150, y=50)  # Ajuste x et y pour la position voulue

# Optionnel : ajouter du texte ou un symbole sur la 3ème carte
carte3.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 4eme carte dealer
carte4 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
carte4.place(x=200, y=50)

# Optionnel : ajouter du texte ou un symbole sur la 4ème carte
carte4.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

#-------------------------------------------------------------- Cartes du joueur --------------------------------------------------------------#





# Outline de la 2eme carte dealer, face cachée
carteJ2 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
carteJ2.place(x=100, y=5)

# Optionnel : ajouter du texte ou un symbole sur la 2ème carte
carteJ2.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 3ème carte dealer, superposée
carteJ3 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
carteJ3.place(x=150, y=5)  # Ajuste x et y pour la position voulue

# Optionnel : ajouter du texte ou un symbole sur la 3ème carte
carteJ3.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 4eme carte dealer
carteJ4 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
carteJ4.place(x=200, y=5)

# Optionnel : ajouter du texte ou un symbole sur la 4ème carte
carteJ4.create_text(100, 150, text="?", font=("Arial", 60), fill="black")
'''