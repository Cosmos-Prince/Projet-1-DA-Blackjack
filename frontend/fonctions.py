import random
from Cartes import *
from Acteurs import *
import tkinter as tk

def creer_deck():
        # Rassemble toutes les cartes déjà créées
        toutes_les_cartes = [
            HA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK,
            DA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK,
            SA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK,
            CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK
        ]
        random.shuffle(toutes_les_cartes)
        return toutes_les_cartes


# Fonction pour afficher les cartes
def afficherCarte(carte:Cartes):
    #Collection des infos de la carte & mise dans des variables Tkinter
    chiffre_var = tk.StringVar()
    symbole_var = tk.StringVar()
    couleur_var = tk.StringVar()
    chiffre_var.set(carte.getChiffre())
    symbole_var.set(carte.getSymboleAffichage())
    couleur_var.set(carte.getCouleur())
