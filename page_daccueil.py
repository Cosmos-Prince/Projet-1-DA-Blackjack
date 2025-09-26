import tkinter as tk
from Acteurs import *
from fonctions import *
from BlackJack import *

#effet sur boutto
def bouton_personnalise(parent, text, command=None, bg="#ffffff", fg="#000000", hover_bg='green'):
    #effet de petite couleur quand tu clique desuss
    def on_enter(e):
        btn.config(bg=hover_bg)
    def on_leave(e):
        btn.config(bg=bg)
    
    #parametre bputton
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 30, "bold"),
        bg=bg,
        fg=fg,
        activebackground=hover_bg,
        activeforeground=fg,
        relief="flat",
        padx=25,
        pady=15,
        bd=0,
        cursor="hand2"
    )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn


def newGame():
    game:BlackJack = BlackJack(Acceuil)
    game.nouvelle_partie()


# Initialisation de la fenêtre
global Acceuil
Acceuil = tk.Tk()

# Titre de la fenêtre
Acceuil.title("Black Jack")

# Taille de la fenêtre
largeur= Acceuil.winfo_screenwidth()               
hauteur= Acceuil.winfo_screenheight()
Acceuil.geometry("%dx%d" %(largeur, hauteur))

# Définir la couleur de fond en vert
Acceuil.configure(bg="#085b18")

# Charger l'image
bg_image = tk.PhotoImage(file="blackjack2.png")

# Mettre l'image en arrière-plan
background_label = tk.Label(Acceuil, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()

# Création du frame du titre
frameTitre = tk.Frame(Acceuil, bg="#0b7821", padx=20, pady=20, height=100, width=(largeur - 0))
frameTitre.place(x=0, y=0)

# Ajouter un titre dans le haut
titre_label = tk.Label(frameTitre, text="Black Jack", font=("Algerian", 80),bg="#0b7821", fg="#7cff85")
titre_label.place(relx=0.5, rely=0.55, anchor="center")  

#Boutton pour commencer a jpuer
boutton_distribuer = bouton_personnalise(Acceuil, text="Jouer" , command=newGame)
boutton_distribuer.place(relx=0.6, rely=0.6, anchor="center")

#liste nombre de joueur

choix_joueurs = tk.StringVar()
choix_joueurs.set("Choisir le nombre de joueurs")  # Texte par défaut

liste = tk.OptionMenu(Acceuil, choix_joueurs, "1 joueur")
liste.config(font=("Arial", 12), bg="white", fg="black", width=25, height=4)
liste.place(relx=0.4, rely=0.6, anchor="center")

#bouton d'infos
from tkinter import messagebox

def afficher_regles():
    regles = (
        "Règles du Blackjack :\n\n"
        "- Approchez-vous le plus possible de 21 sans dépasser\n"
        "- Les As valent 1 ou 11, les figures valent 10.\n"
        "- Le croupier tire obligatoirement jusqu'à 16 et s'arrête à 17.\n"
        "- Le Blackjack (21 avec 2 cartes) bat un 21 normal.\n"
    )
    messagebox.showinfo("Règles du Blackjack", regles)



# Bouton "i"
btn_info = bouton_personnalise(Acceuil, text="i", command=afficher_regles)
btn_info.place(relx=0.9, rely=0.1, anchor="center")

# Label accrocheur sans fond
label_accroche = tk.Label(
    Acceuil,
    text=" Venez jouer à notre jeu de Blackjack !",
    font=("Arial", 40, "bold"),
    fg="black"  # texte doré style casino
)
label_accroche.place(relx=0.5, rely=0.4, anchor="center")


Acceuil.mainloop()