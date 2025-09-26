import tkinter as tk
from affichageCartes import *
#from TurnOrder import *
from fonctions import *
from Cartes import *
from Acteurs import *

'''
*** MODIFICATIONS DE LA FONCTION CARTE_JOUEUR CAR DES AJOUTS ONT ÉTÉ APPORTÉS DANS AFFICHAGECARTES.PY ***
'''
# Affichage d'une carte dans le frame des cartes pour le joueur 
def carte_joueur(numero_carte: int, carte: Cartes):
    affichageCarte(frameCartesJoueur, carte, x=50*(numero_carte-1))

'''
*** MODIFICATIONS DE CHOISIR_TIRER() ***
'''
# Logique lorsque le boutton "hit" est appuyé
def choisir_tirer():

    global deck, Player1 # Utilisation des variables globales pour accéder au deck et au joueur
    Player1.ajouter_carte(deck.pop())  # Ajoute une carte à la main du joueur
    carte_joueur(len(Player1.main), Player1.main[-1])  # Affiche la carte à la dernière position de la main
    updateScoreJoueur()    # Met à jour le score du joueur

    # vérification si le joueur a dépassé 21 (réutilisable aussi pour le dealer)
    if acteur_est_bust(Player1): # Utilise la fonction de fonctions.py
        tour_label.config(text="Vous avez dépassé 21 (Bust). Manche terminée.")

        #Unpack les bouttons qui permettent de tirer et de rester
        bouton_tirer.config(state="disabled")
        bouton_rester.config(state="disabled")


'''
*** MODIFICATIONS DE CHOISIR_RESTER() ***
'''
# Logique lorsque le boutton "stay" est appuyé
def choisir_rester():
    #Unpack les boutons qui permettent de tirer et rester
    bouton_tirer.config(state="disabled")
    bouton_rester.config(state="disabled")

    global deck, Dealer # Utilisation des variables globales pour accéder au deck et au croupier

    # si le croupier n’a pas encore de cartes visibles, on lui en met 2
    if len(Dealer.main) == 0: # Vérifie si le croupier a des cartes
        Dealer.ajouter_carte(deck.pop()); carte_dealer(1, Dealer.main[0]) # Affiche la première carte du croupier
        Dealer.ajouter_carte(deck.pop()); carte_dealer(2, Dealer.main[1]) # Affiche la deuxième carte du croupier

    # mémorise combien il avait de cartes avant de piocher
    mémoire_nb_cartes = len(Dealer.main)

    # Révéler la 2e carte cachée du dealer
    for carte in frameCartesDealer.winfo_children(): # Parcourt les cartes du dealer
        carte.destroy()  # efface les cartes actuelles
    carte_dealer(1, Dealer.main[0]) # Affiche la première carte du croupier
    carte_dealer(2, Dealer.main[1]) # Affiche la deuxième carte du croupier

    global dealer_carte_cachee # Accède à la variable globale pour la carte cachée

    # Révéler la 2e carte si elle est cachée
    if dealer_carte_cachee is not None: 
        dealer_carte_cachee.destroy() # Supprime le dos de la carte
        dealer_carte_cachee = None # Réinitialise la variable
        carte_dealer(2, Dealer.main[1])  # on dessine la vraie 2e carte

    # le croupier joue tout seul (jusqu'à 17)
    tour_croupier(Dealer, deck)

    # dessine uniquement les nouvelles cartes tirées
    for i in range(mémoire_nb_cartes, len(Dealer.main)): 
        carte_dealer(i + 1, Dealer.main[i]) # Affiche les nouvelles cartes du croupier

    # verdict de la manche
    score_joueur = Player1.getScore() # Récupère le score du joueur
    score_dealer = Dealer.getScore() # Récupère le score du croupier
    if acteur_est_bust(Dealer): # fonction de fonctions.py
        verdict = "Vous avez gagné !"  # dealer bust
    elif score_joueur > score_dealer:
        verdict = "Vous avez gagné !"
    elif score_joueur < score_dealer:
        verdict = "Vous avez perdu"
    else:
        verdict = "Égalité (push)"
    tour_label.config(text=f"Résultat — Joueur: {score_joueur} | Croupier: {score_dealer} → {verdict}")


'''
*** AJOUT DE LA FONCTION NOUVELLE_PARTIE() ***
'''
# Fonction pour démarrer une nouvelle partie
def nouvelle_partie():
    #Pack les boutons
    bouton_rester.config(state="normal")
    bouton_tirer.config(state="normal")


    global deck, Player1, Dealer # Utilisation des variables globales pour accéder au deck et aux acteurs

    # Réinitialiser deck et acteurs
    deck = creer_deck()
    Player1 = Joueur("Joueur 1")
    Dealer = Croupier()

    # Effacer les anciennes cartes affichées
    for carte in frameCartesJoueur.winfo_children(): # winfo_children() retourne une liste de tous les widgets (items) enfants du joueur
        carte.destroy() # efface les cartes actuelles
    for carte in frameCartesDealer.winfo_children(): # winfo_children() retourne une liste de tous les widgets (items) enfants du dealer
        carte.destroy() # efface les cartes actuelles

    # Réinitialiser le score affiché
    updateScoreJoueur() # Met à jour le score du joueur
    tour_label.config(text="Nouvelle partie — À votre tour : Tirer ou rester") # Réinitialise le label du tour

    global dealer_cache_canvas

    # Nettoyer l'affichage dealer
    for c in frameCartesDealer.winfo_children():
        c.destroy()

    # Dealer : 1 carte visible + 1 dos
    Dealer.ajouter_carte(deck.pop())
    carte_dealer(1, Dealer.main[0])
    Dealer.ajouter_carte(deck.pop())
    dealer_cache_canvas = carte_dos_dealer(2)  # on mémorise le dos pour le révéler plus tard

    # Distribuer 2 cartes au joueur
    Player1.ajouter_carte(deck.pop())
    carte_joueur(1, Player1.main[0])
    Player1.ajouter_carte(deck.pop())
    carte_joueur(2, Player1.main[1])
    updateScoreJoueur()

    # Vérifie si le joueur a blackjack et le fait rester automatiquement si c'est le cas
    if Player1.getScore() == 21:
        choisir_rester()


#Utilise la fonction ci haut pour updater avec des variables globales
def updateScoreJoueur():
    global scoreMainJoueurLabel
    global Player1
    updateScore(scoreMainJoueurLabel, Player1)

'''
*** MODIFICATIONS DE LA FONCTION CARTE_DEALER CAR DES AJOUTS ONT ÉTÉ APPORTÉS DANS AFFICHAGECARTES.PY ***
'''
# Affichage pour les cartes du dealer
def carte_dealer(numero_carte: int, carte: Cartes):
    affichageCarte(frameCartesDealer, carte, x=50*(numero_carte-1))

'''
*** AJOUT DE LA FONCTION CARTE_DOS_DEALER() ***
'''
# Affichage d'une carte face cachée pour le dealer
def carte_dos_dealer(numero_carte: int): 
    # Création d'un Canvas pour la carte face cachée
    card = tk.Canvas(frameCartesDealer, width=200, height=300, bg="#c0c0c0", 
                     highlightthickness=2, highlightbackground="black") 
    card.place(x=50 * (numero_carte - 1), y=5) # Positionne la carte dans le frame du dealer
    card.create_rectangle(10, 10, 190, 290, outline="black") # Bordure de la carte
    card.create_text(100, 150, text="?", font=("Arial", 60), fill="black") # Symbole central
    return card



#Création des instances pour la partie, elles sont utilisées dans plusieurs fonctions à l'aide de global
deck:list = creer_deck()
Player1:Joueur = Joueur("Joueur 1")
Dealer:Croupier = Croupier()
dealer_carte_cachee = None  # Variable pour stocker la carte face cachée du dealer


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
frameDealer = tk.Frame(frameJeu, bg="#0b7821", height=400, width=(largeur - 150))
frameDealer.place(x=0, y=50)

# Création d'une frame pour le joueur
frameJoueur = tk.Frame(frameJeu, bg="#0b7821", height=400, width=(largeur - 150))
frameJoueur.place(x=0, y=525)

# Frame pour afficher le score du joueur
frameScoreMainJoueur = tk.Frame(frameJoueur, bg="#0b7821", padx=20, pady=20, height=400, width=250)
frameScoreMainJoueur.place(relx=0.87, y=0)

# Label pour afficher le score de la main du joueur
scoreMainJoueurLabel = tk.Label(frameScoreMainJoueur, text=f"Score: {Player1.getScore()}", font=("Arial", 16), bg="#0b7821", fg="white")
scoreMainJoueurLabel.place(relx=0.5, rely=0.5, anchor="center")

# Frame pour les cartes du joueur
frameCartesJoueur = tk.Frame(frameJoueur, bg="#0b7821", padx=20, pady=20, height=400, width=500)
frameCartesJoueur.place(relx=0.36, y=0)  # Centré horizontalement

# Frame pour afficher le total des victoires du dealer & du joueur
frameScoreTotal = tk.Frame(frameDealer, bg="#0b7821", padx=20, pady=20, height=400, width=400)
frameScoreTotal.place(relx=0, y=0)  # <-- Modifié pour être plus à gauche

# Label pour afficher le score total du dealer
scoreTotalDealerLabel = tk.Label(frameScoreTotal, text="Victoires totales Dealer: 0", font=("Arial", 16), bg="#0b7821", fg="white")
scoreTotalDealerLabel.place(relx=0.5, rely=0.3, anchor="center")  # Centré

# Label pour afficher le score total du joueur
scoreTotalJoueurLabel = tk.Label(frameScoreTotal, text="Victoires totales Joueur: 0", font=("Arial", 16), bg="#0b7821", fg="white")
scoreTotalJoueurLabel.place(relx=0.5, rely=0.7, anchor="center")  # Centré

# Frame pour les cartes du dealer
frameCartesDealer = tk.Frame(frameDealer, bg="#0b7821", padx=20, pady=20, height=400, width=500)
frameCartesDealer.place(relx=0.36, y=0)  # Centré horizontalement

# Label pour indiquer le tour au joueur
tour_label = tk.Label(frameJeu, text="À votre tour : Tirer ou rester", font=("Arial", 20), bg="#0b7821", fg="#ffffff")
tour_label.place(relx=0.75, y=75, anchor="center")  # Centré horizontalement


'''
=====================================
FRAMES POUR LES BOUTTONS
=====================================
'''
# Création d'une frame pour les boutons
frameBoutons = tk.Frame(frameJeu, bg="#0b7821", height=100, width=(largeur - 150))
frameBoutons.place(x=0, y=400)   # entre dealer et joueur

# Création du bouton tirer une carte (dans frameBoutons)
bouton_tirer = tk.Button(frameBoutons, text="Tirer", font=("Arial", 16), bg="#4CAF50", fg="white", padx=10, pady=5, command=choisir_tirer)
bouton_tirer.place(relx=0.38, rely=0.5, anchor="center")
  # Centré verticalement et à gauche

# Création du bouton rester (dans frameBoutons)
bouton_rester = tk.Button(frameBoutons, text="Rester", font=("Arial", 16), bg="#f44336", fg="white", padx=10, pady=5, command=choisir_rester)
bouton_rester.place(relx=0.52, rely=0.5, anchor="center")

'''
*** AJOUT DU BOUTON NOUVELLE_PARTIE() ***
'''
# Création du bouton nouvelle partie (dans frameBoutons)
bouton_nouvelle_partie = tk.Button(frameBoutons,text="Nouvelle partie",font=("Arial", 16),bg="#2196F3",fg="white",padx=10,pady=5,command=nouvelle_partie)
bouton_nouvelle_partie.place(relx=0.66, rely=0.5, anchor="center")


'''
MODIFICATIONS ET AJOUT
'''

# Joueur : 2 cartes visibles
Player1.ajouter_carte(deck.pop())
carte_joueur(1, Player1.main[0])
Player1.ajouter_carte(deck.pop())
carte_joueur(2, Player1.main[1])
updateScoreJoueur()

# Dealer : 1 carte visible + 1 carte cachée
Dealer.ajouter_carte(deck.pop()) # Carte visible
carte_dealer(1, Dealer.main[0]) # Affiche la première carte du croupier
Dealer.ajouter_carte(deck.pop()) # Carte cachée
carte_cachee = carte_dos_dealer(2)  # Affiche la carte face cachée


# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
