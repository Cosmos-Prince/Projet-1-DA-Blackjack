from Cartes import *
import tkinter as tk


'''
=====================================
DEVRAIT UTILISER CE FICHIER POUR AFFICHER TOUTES LES CARTES, MAIS DOIT UPDATE LE Y DU PLACEMENT + CHANGER PACK() -> PLACE()
=====================================
'''


def affichageCarte(fenetre:tk.Frame, carte:Cartes):
    chiffre = carte.getChiffre()
    symbole = carte.getSymboleAffichage()
    couleur = carte.getCouleur()

    #Outline de la carte
    card = tk.Canvas(fenetre, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
    card.pack(pady=30)

    # Texte en haut à gauche
    card.create_text(20, 20, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="nw")
    card.create_text(20, 45, text= symbole, font=("Arial", 20), fill= couleur, anchor="nw")

    # Texte en bas à droite (retourné)
    card.create_text(180, 280, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="se")
    card.create_text(180, 255, text= symbole, font=("Arial", 20), fill= couleur, anchor="se")

    # Symbole central
    card.create_text(100, 150, text= symbole, font=("Arial", 60), fill= couleur)



































































































































































