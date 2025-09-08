import tkinter as tk

# Initialisation de la fenêtre
fenetre = tk.Tk()

carteObtenue = tk.StringVar()
chiffre = tk.StringVar()
couleur = tk.StringVar()
symbole = tk.StringVar()

# Détermine la couleur et le symbole selon la carte obtenue
if carteObtenue.get() == "Carreau":
    couleur = "red"
    symbole = "♦"
elif carteObtenue.get() == "Coeur":
    couleur = "red"
    symbole = "♥"
elif carteObtenue.get() == "Pique":    
    couleur = "black"
    symbole = "♠"
elif carteObtenue.get() == "Trefle":
    couleur = "black"
    symbole = "♣"
else:
    print("wtf")

# As de coeur
as_de_coeur = tk.Canvas(fenetre, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
as_de_coeur.pack(pady=30)

# Texte en haut à gauche
as_de_coeur.create_text(20, 20, text= chiffre.get(), font=("Arial", 20, "bold"), fill= couleur.get(), anchor="nw")
as_de_coeur.create_text(20, 45, text= symbole.get(), font=("Arial", 20), fill= couleur.get(), anchor="nw")

# Texte en bas à droite (retourné)
as_de_coeur.create_text(180, 280, text= chiffre.get(), font=("Arial", 20, "bold"), fill= couleur.get(), anchor="se")
as_de_coeur.create_text(180, 255, text= symbole.get(), font=("Arial", 20), fill= couleur.get(), anchor="se")

# Symbole central
as_de_coeur.create_text(100, 150, text= symbole.get(), font=("Arial", 60), fill= couleur.get())



































































































































































fenetre.mainloop()