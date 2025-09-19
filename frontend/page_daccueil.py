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


fenetre.mainloop()