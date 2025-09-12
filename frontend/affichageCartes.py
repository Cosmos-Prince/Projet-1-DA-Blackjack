import tkinter as tk

# Initialisation de la fenêtre
fenetre = tk.Tk()

carteObtenue = tk.StringVar()
chiffre = tk.StringVar()
couleur = tk.StringVar()
symbole = tk.StringVar()


# pour tests, à enlever
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

# As de coeur
as_de_coeur = tk.Canvas(fenetre, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
as_de_coeur.pack(pady=30)

# Texte en haut à gauche
as_de_coeur.create_text(20, 20, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="nw")
as_de_coeur.create_text(20, 45, text= symbole, font=("Arial", 20), fill= couleur, anchor="nw")

# Texte en bas à droite (retourné)
as_de_coeur.create_text(180, 280, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="se")
as_de_coeur.create_text(180, 255, text= symbole, font=("Arial", 20), fill= couleur, anchor="se")

# Symbole central
as_de_coeur.create_text(100, 150, text= symbole, font=("Arial", 60), fill= couleur)



































































































































































fenetre.mainloop()