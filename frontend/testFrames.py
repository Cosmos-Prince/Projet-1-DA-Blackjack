import tkinter as tk

# Initialisation de la fenêtre
fenetre = tk.Tk()

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
frameScoreTotal = tk.Frame(frameDealer, bg="#ff0000", padx=20, pady=20, height=400, width=250)
frameScoreTotal.place(relx=0.87, y=0)

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







fenetre.mainloop()

