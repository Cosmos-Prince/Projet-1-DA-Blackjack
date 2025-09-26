import tkinter as tk
import affichageCartes as ac
from tkinter import PhotoImage

# Initialisation de la fenêtre
fenetre = tk.Tk()

# Initialisation des variables pour la carte
carteObtenue = tk.StringVar()
chiffre = tk.StringVar()
couleur = tk.StringVar()
symbole = tk.StringVar()

# Titre de la fenêtre
fenetre.title("Black Jack")

# Taille de la fenêtre
largeur= fenetre.winfo_screenwidth()               
hauteur= fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" %(largeur, hauteur))

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

# Création d'une frame pour les boutons
frameBoutons = tk.Frame(frameJeu, bg="#0400ff", padx=20, pady=20, height=100, width=(largeur - 150))
frameBoutons.place(x=0, y=450)

# Création d'une frame pour le joueur
frameJoueur = tk.Frame(frameJeu, bg="#ffffff", height=400, width=(largeur - 150))
frameJoueur.place(x=0, y=525)

# Création du bouton tirer une carte (dans frameBoutons)
bouton_tirer = tk.Button(frameBoutons, text="Tirer", font=("Arial", 16), bg="#4CAF50", fg="white", padx=10, pady=5)
bouton_tirer.place(relx=0.45, rely=0.3, anchor="center")  # Centré verticalement et à gauche

# Création du bouton rester (dans frameBoutons)
bouton_rester = tk.Button(frameBoutons, text="Rester", font=("Arial", 16), bg="#f44336", fg="white", padx=10, pady=5)
bouton_rester.place(relx=0.55, rely=0.3, anchor="center")  # Centré verticalement et à droite

# Frame pour afficher le score du joueur
frameScoreMainJoueur = tk.Frame(frameJoueur, bg="#ff0000", padx=20, pady=20, height=400, width=250)
frameScoreMainJoueur.place(relx=0.87, y=0)

# Label pour afficher le score de la main du joueur
scoreMainJoueurLabel = tk.Label(frameScoreMainJoueur, text="Score: 0", font=("Arial", 16), bg="#ff0000", fg="white")
scoreMainJoueurLabel.place(relx=0.5, rely=0.5, anchor="center")

# Frame pour les cartes du joueur
frameCartesJoueur = tk.Frame(frameJoueur, bg="#00ff00", padx=20, pady=20, height=400, width=500)
frameCartesJoueur.place(relx=0.36, y=0)  # Centré horizontalement

# Test
couleur, symbole, chiffre = ac.determinerCouleurSymbole("Pique", "J")

#-------------------------------------------------------------- Cartes du dealer --------------------------------------------------------------#

# Outline de la 1ere carte dealer
carte1 = tk.Canvas(frameCartesDealer, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
carte1.place(x=50, y=50)

# Texte en haut à gauche
carte1.create_text(20, 20, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="nw")
carte1.create_text(20, 45, text=symbole, font=("Arial", 20), fill=couleur, anchor="nw")
carte1.create_text(180, 280, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="se")
carte1.create_text(180, 255, text=symbole, font=("Arial", 20), fill=couleur, anchor="se")
carte1.create_text(100, 150, text=symbole, font=("Arial", 60), fill=couleur)

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
# Outline de la 1ere carte joueur
carteJ1 = tk.Canvas(frameCartesJoueur, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
carteJ1.place(x=50, y=5)
# Texte en haut à gauche
carteJ1.create_text(20, 20, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="nw")
carteJ1.create_text(20, 45, text=symbole, font=("Arial", 20), fill=couleur, anchor="nw")
carteJ1.create_text(180, 280, text=chiffre, font=("Arial", 20, "bold"), fill=couleur, anchor="se")
carteJ1.create_text(180, 255, text=symbole, font=("Arial", 20), fill=couleur, anchor="se")
carteJ1.create_text(100, 150, text=symbole, font=("Arial", 60), fill=couleur)

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

#-------------------------------------------------------------- Jetons --------------------------------------------------------------#
frameJetons = tk.Frame(frameDealer, bg="#ffff00", padx=20, pady=20, height=400, width=700)
frameJetons.place(relx=0.642, y=0) # <-- Modifié pour être plus à droite

image = PhotoImage(file="frontend/jetons.png")
label_image = tk.Label(frameJetons, image=image)
label_image.image = image  # Nécessaire pour éviter que l'image soit supprimée par le garbage collector
label_image.place(x=100, y=100)




fenetre.mainloop()

