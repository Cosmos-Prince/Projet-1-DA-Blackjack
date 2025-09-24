import tkinter as tk
from affichageCartes import *
#from TurnOrder import *
from fonctions import *
from Cartes import *
from Acteurs import *


# Affichage d'une carte dans le frame des cartes pour le joueur 
def carte_joueur(numero_carte: int, carte:Cartes):
    chiffre = carte.getChiffre()
    symbole = carte.getSymboleAffichage()
    couleur = carte.getCouleur()
    # Appelle les getters pour obtenir les valeurs de la carte pour l'affichage

    card = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
    card.place(x=50 * numero_carte, y=5)

    # Création d'une carte
    card.create_text(20, 20, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="nw")
    card.create_text(20, 45, text=symbole, font=("Arial", 20), fill=couleur, anchor="nw")
    card.create_text(180, 280, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="se")
    card.create_text(180, 255, text=symbole, font=("Arial", 20), fill=couleur, anchor="se")
    card.create_text(100, 150, text=symbole, font=("Arial", 60), fill=couleur)

# Logique lorsque le boutton "hit" est appuyé
def choisir_tirer():
    # Utilise des variables globales pour changer les valeurs hors de la fonction
    global deck 
    global Player1
    Player1.ajouter_carte(deck.pop())   #Ajoute une carte à la main du joueur
    carte_joueur(len(Player1.main), Player1.main[len(Player1.main)-1])  #Affiche la carte à la derniere position de la main, choisit la derniere carte de la main
    updateScoreJoueur() #voir fonction, update le label qui affiche le score de la main du joueur

# Logique lorsque le boutton "stay" est appuyé
def choisir_rester():
    pass

'''
=====================================
        TO DO
=====================================
'''

# Code réutilisable pour updater le score d'un acteur (joueur ou croupier)
def updateScore(label:tk.Label, acteur:Acteur):
    label.config(text = f"Score : {acteur.getScore()}") #.config permets de changer une valeur sans re créer le label au complet


#Utilise la fonction ci haut pour updater avec des variables globales
def updateScoreJoueur():
    global scoreMainJoueurLabel
    global Player1
    updateScore(scoreMainJoueurLabel, Player1)

# Affichage pour les cartes du dealer
def carte_dealer(numero_carte: int, carte:Cartes):
    chiffre = carte.getChiffre()
    symbole = carte.getSymboleAffichage()
    couleur = carte.getCouleur()

    card = tk.Canvas(frameCartesDealer, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
    card.place(x=50 * numero_carte, y=50)

    # Texte en haut à gauche
    card.create_text(20, 20, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="nw")
    card.create_text(20, 45, text=symbole, font=("Arial", 20), fill=couleur, anchor="nw")
    card.create_text(180, 280, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="se")
    card.create_text(180, 255, text=symbole, font=("Arial", 20), fill=couleur, anchor="se")
    card.create_text(100, 150, text=symbole, font=("Arial", 60), fill=couleur)


#Création des instances pour la partie, elles sont utilisées dans plusieurs fonctions à l'aide de global
deck:list = creer_deck()
Player1:Joueur = Joueur("Joueur 1")
Dealer:Croupier = Croupier()


# Initialisation de la fenêtre
fenetre = tk.Tk()
# Titre de la fenêtre
fenetre.title("Black Jack")
# Taille de la fenêtre
largeur= fenetre.winfo_screenwidth()               
hauteur= fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" %(largeur, hauteur))

'''
=====================================
PLACEMENT DES FRAMES, BACKGROUND, ETC
=====================================
'''

# Définir la couleur de fond en vert
fenetre.configure(bg="#085b18")

# Création d'une première Frame qui va faire la bordure
frameBordure = tk.Frame(fenetre, bg="#5d5103", width=(largeur - 100), height=(hauteur - 150))
frameBordure.place(x=50, y=50)

# Création du frame principal pour le jeu
frameJeu = tk.Frame(frameBordure, bg="#0b7821", width=(largeur - 150), height=(hauteur - 200))
frameJeu.place(x=25, y=25)

# Création du frame du titre
frameTitre = tk.Frame(frameJeu, bg="#0b7821", padx=20, pady=20, height=100, width=(largeur - 150))
frameTitre.place(x=0, y=0)

# Ajouter un titre dans le haut
titre_label = tk.Label(frameTitre, text="Black Jack", font=("Algerian", 24),bg="#0b7821", fg="#7cff85")
titre_label.place(relx=0.5, rely=0.2, anchor="center")  # Centré en haut

# Création d'une frame pour le dealer
frameDealer = tk.Frame(frameJeu, bg="#ffffff", height=400, width=(largeur - 150))
frameDealer.place(x=0, y=50)

# Création d'une frame pour le joueur
frameJoueur = tk.Frame(frameJeu, bg="#ffffff", height=400, width=(largeur - 150))
frameJoueur.place(x=0, y=525)

# Frame pour afficher le score du joueur
frameScoreMainJoueur = tk.Frame(frameJoueur, bg="#ff0000", padx=20, pady=20, height=400, width=250)
frameScoreMainJoueur.place(relx=0.87, y=0)

# Label pour afficher le score de la main du joueur
scoreMainJoueurLabel = tk.Label(frameScoreMainJoueur, text=f"Score: 5{Player1.getScore()}", font=("Arial", 16), bg="#ff0000", fg="white")
scoreMainJoueurLabel.place(relx=0.5, rely=0.5, anchor="center")

# Frame pour les cartes du joueur
frameCartesJoueur = tk.Frame(frameJoueur, bg="#00ff00", padx=20, pady=20, height=400, width=500)
frameCartesJoueur.place(relx=0.36, y=0)  # Centré horizontalement

# Frame pour afficher le total des victoires du dealer & du joueur
frameScoreTotal = tk.Frame(frameDealer, bg="#ff0000", padx=20, pady=20, height=400, width=400)
frameScoreTotal.place(relx=0, y=0)  # <-- Modifié pour être plus à gauche

# Label pour afficher le score total du dealer
scoreTotalDealerLabel = tk.Label(frameScoreTotal, text="Victoires totales Dealer: 0", font=("Arial", 16), bg="#ff0000", fg="white")
scoreTotalDealerLabel.place(relx=0.5, rely=0.3, anchor="center")  # Centré

# Label pour afficher le score total du joueur
scoreTotalJoueurLabel = tk.Label(frameScoreTotal, text="Victoires totales Joueur: 0", font=("Arial", 16), bg="#ff0000", fg="white")
scoreTotalJoueurLabel.place(relx=0.5, rely=0.7, anchor="center")  # Centré

# Frame pour les cartes du dealer
frameCartesDealer = tk.Frame(frameDealer, bg="#00ff00", padx=20, pady=20, height=400, width=500)
frameCartesDealer.place(relx=0.36, y=0)  # Centré horizontalement

# Label pour indiquer le tour au joueur
tour_label = tk.Label(frameJeu, text="À votre tour : Tirer ou rester", font=("Arial", 20), bg="#0b7821", fg="#ffffff")
tour_label.place(relx=0.5, y=75, anchor="center")  # Centré horizontalement

#choix_joueur = tk.StringVar(value="")  # Variable pour stocker le choix

    
#-------------------------------------------------------------- Cartes du dealer --------------------------------------------------------------#

# Outline de la 1ere carte dealer


# Outline de la 2eme carte dealer, face cachée
#carte2 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
#carte2.place(x=100, y=50)

# Optionnel : ajouter du texte ou un symbole sur la 2ème carte
#carte2.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 3ème carte dealer, superposée
#carte3 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
#carte3.place(x=150, y=50)  # Ajuste x et y pour la position voulue

# Optionnel : ajouter du texte ou un symbole sur la 3ème carte
#carte3.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 4eme carte dealer
#carte4 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
#carte4.place(x=200, y=50)

# Optionnel : ajouter du texte ou un symbole sur la 4ème carte
#carte4.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

#-------------------------------------------------------------- Cartes du joueur --------------------------------------------------------------#





# Outline de la 2eme carte dealer, face cachée
#carteJ2 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
#carteJ2.place(x=100, y=5)

# Optionnel : ajouter du texte ou un symbole sur la 2ème carte
#carteJ2.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 3ème carte dealer, superposée
#carteJ3 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
#carteJ3.place(x=150, y=5)  # Ajuste x et y pour la position voulue

# Optionnel : ajouter du texte ou un symbole sur la 3ème carte
#carteJ3.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

# Outline de la 4eme carte dealer
#carteJ4 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="yellow", highlightthickness=2, highlightbackground="black")
#carteJ4.place(x=200, y=5)

# Optionnel : ajouter du texte ou un symbole sur la 4ème carte
#carteJ4.create_text(100, 150, text="?", font=("Arial", 60), fill="black")

'''
=====================================
FRAMES POUR LES BOUTTONS
=====================================
'''
# Création d'une frame pour les boutons
frameBoutons = tk.Frame(frameJeu, bg="#0400ff", padx=20, pady=20, height=100, width=(largeur - 150))
frameBoutons.place(x=0, y=450)


# Création du bouton tirer une carte (dans frameBoutons)
bouton_tirer = tk.Button(frameBoutons, text="Tirer", font=("Arial", 16), bg="#4CAF50", fg="white", padx=10, pady=5, command=choisir_tirer)
bouton_tirer.place(relx=0.45, rely=0.3, anchor="center")  # Centré verticalement et à gauche

# Création du bouton rester (dans frameBoutons)
bouton_rester = tk.Button(frameBoutons, text="Rester", font=("Arial", 16), bg="#f44336", fg="white", padx=10, pady=5, command=choisir_rester)
bouton_rester.place(relx=0.55, rely=0.3, anchor="center")  # Centré verticalement et à droite

#------------------------------------------------------------- Début de l'intégration du BackEnd --------------------------------------------------------------#
'''
# Démarrer le jeu en appelant la fonction du backend
def demarrer_jeu():
    be.gerer_les_tours()

bouton_demarrer = tk.Button(frameBoutons, text="Démarrer la partie", font=("Arial", 16), bg="#2196F3", fg="white", command=demarrer_jeu)
bouton_demarrer.place(relx=0.5, rely=0.7, anchor="center")
'''
# Test
#carte_dealer(1, DK)
#carte_dealer(2, C10)

Player1.ajouter_carte(deck.pop())
carte_joueur(1, Player1.main[0])
Player1.ajouter_carte(deck.pop())
carte_joueur(2, Player1.main[1])
updateScoreJoueur()


# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
