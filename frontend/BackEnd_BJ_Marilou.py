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

