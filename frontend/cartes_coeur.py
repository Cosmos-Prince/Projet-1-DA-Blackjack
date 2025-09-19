import tkinter as tk

# Initialisation de la fenêtre
fenetre = tk.Tk()

# Titre de la fenêtre
fenetre.title("Black Jack")

# Taille de la fenêtre
fenetre.attributes('-fullscreen', True)

# Hauteur de la fenêtre : 1080 pixels
# Largeur de la fenêtre : 1920 pixels

# Définir la couleur de fond en vert
fenetre.configure(bg="green")

# Création d'une première Frame qui va occuper le haut de la page
haut_frame = tk.Frame(fenetre, bg="brown", height=80)
haut_frame.pack(fill="x")  # Remplit toute la largeur, hauteur fixe

# Ajouter un titre dans le haut
titre_label = tk.Label(haut_frame, text="Black Jack", font=("Arial", 24, "bold"), bg="brown", fg="black")
titre_label.pack(pady=20)

# Création de la frame pour le dealer
dealer_frame = tk.Frame(fenetre, bg="red", height=750 )
dealer_frame.pack(fill="x")

# Création de la frame pour le joueur
joueur_frame = tk.Frame(fenetre, bg="yellow", height=1000)
joueur_frame.pack(fill="x")


# Initialisation des variables
carteObtenue = tk.StringVar()
chiffre = tk.StringVar()
couleur = tk.StringVar()
symbole = tk.StringVar()

#----------------------------------------------------- Valeurs temporaire pour tests ----------------------------------------------------
#                                                           ENLEVER LORSQUE FINI
carteObtenue = "Carreau"
chiffre = "A"

# Détermine la couleur et le symbole selon la carte obtenue
if carteObtenue == "Carreau":
    couleur = "red"
    symbole = "♦"
elif carteObtenue == "Coeur":
    couleur = "red"
    symbole = "♥"
elif carteObtenue == "Pique":    
    couleur = "black"
    symbole = "♠"
elif carteObtenue == "Trefle":
    couleur = "black"
    symbole = "♣"
else:
    print("wtf")

# Création de la 1ere carte dealer
carte = tk.Canvas(dealer_frame, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
carte.pack(pady=30)

# Texte en haut à gauche
carte.create_text(20, 20, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="nw")
carte.create_text(20, 45, text= symbole, font=("Arial", 20), fill= couleur, anchor="nw")

# Texte en bas à droite (retourné)
carte.create_text(180, 280, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="se")
carte.create_text(180, 255, text= symbole, font=("Arial", 20), fill= couleur, anchor="se")

# Symbole central
carte.create_text(100, 150, text= symbole, font=("Arial", 60), fill= couleur)


# Création de la 1ere carte joueur
carte = tk.Canvas(joueur_frame, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
carte.pack(pady=30)

# Texte en haut à gauche
carte.create_text(20, 20, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="nw")
carte.create_text(20, 45, text= symbole, font=("Arial", 20), fill= couleur, anchor="nw")

# Texte en bas à droite (retourné)
carte.create_text(180, 280, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="se")
carte.create_text(180, 255, text= symbole, font=("Arial", 20), fill= couleur, anchor="se")

# Symbole central
carte.create_text(100, 150, text= symbole, font=("Arial", 60), fill= couleur)



































































































































































fenetre.mainloop()