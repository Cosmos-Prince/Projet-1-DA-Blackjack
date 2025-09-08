import tkinter as tk

# Initialisation de la fenêtre
fenetre = tk.Tk()

# Titre de la fenêtre
fenetre.title("Black Jack")

# Taille de la fenêtre
fenetre.geometry("1000x800")

# Définir la couleur de fond en vert
fenetre.configure(bg="green")

# Création d'une première Frame qui va occuper le haut de la page
haut_frame = tk.Frame(fenetre, bg="white", height=80)
haut_frame.pack(fill="x")  # Remplit toute la largeur, hauteur fixe

# Ajouter un titre dans le haut
titre_label = tk.Label(haut_frame, text="Black Jack", font=("Arial", 24, "bold"), bg="white", fg="black")
titre_label.pack(pady=20)

# Affichage du titre Black Jack sur la page




fenetre.mainloop()