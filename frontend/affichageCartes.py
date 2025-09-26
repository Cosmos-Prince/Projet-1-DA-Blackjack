# Fonction qui détermine la couleur et le symbole selon la carte obtenue
def determinerCouleurSymbole(carteObtenue, chiffre):
    couleur = "black"   # Valeur par défaut
    symbole = "?"
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
        print("Carte inconnue :", carteObtenue)
    return couleur, symbole, chiffre

# Outline de la carte
#carte = tk.Canvas(fenetre, width=200, height=300, bg="white", highlightthickness=2, highlightbackground="black")
#carte.pack(pady=30)

# Texte en haut à gauche
#carte.create_text(20, 20, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="nw")
#carte.create_text(20, 45, text= symbole, font=("Arial", 20), fill= couleur, anchor="nw")

# Texte en bas à droite (retourné)
#carte.create_text(180, 280, text= chiffre, font=("Arial", 20, "bold"), fill= couleur, anchor="se")
#carte.create_text(180, 255, text= symbole, font=("Arial", 20), fill= couleur, anchor="se")

# Symbole central
#carte.create_text(100, 150, text= symbole, font=("Arial", 60), fill= couleur)



































































































































































