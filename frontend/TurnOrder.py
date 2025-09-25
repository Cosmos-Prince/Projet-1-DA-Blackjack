from fonctions import *


# Fonction pour gérer les tours des joueur
def tour_joueur(joueur:Joueur, deck):
    # Tour d'un joueur à la fois
    '''
    while calculer_score(joueur.main) < 21:
        #print(f"\nMain de {joueur.nom}: {joueur.afficher_main()} (Score: {calculer_score(joueur.main)})")
        
        action = choix_joueur.get()
        if action == "tirer":
            # Fonction pop() pour retirer du deck la carte piochée
            joueur.ajouter_carte(deck.pop())

            # Affichage de la carte piochée
            carte_piochée : Cartes = joueur.main[-1]
            chiffre_var = tk.StringVar()
            symbole_var = tk.StringVar()
            couleur_var = tk.StringVar()
            chiffre_var.set(carte_piochée.getChiffre()chiffre)
            symbole_var.set(carte_piochée.getSymboleAffichage())
            couleur_var.set(carte_piochée.getCouleur())

            carte_joueur(len(joueur.main), chiffre, couleur, symbole)
        else:
            break
        '''




# Fonction pour gérer le tour du croupier
def tour_croupier(croupier, deck):
    print(f"\nMain du croupier (cachée): {croupier.afficher_main(reveal=False)}")
    while calculer_score(croupier.main) < 17:
        # Fonction pop() pour retirer du deck la carte piochée
        croupier.ajouter_carte(deck.pop())
        print(f"Croupier tire et obtient (Score: {calculer_score(croupier.main)})")
    print(f"Main du croupier (révélée): {croupier.afficher_main(reveal=True)} "
          f"(Score: {calculer_score(croupier.main)})")



# Fonction pour gérer les tours entre joueur et croupier
def gerer_les_tours():
    # Création du deck, joueur, et croupier
    deck = creer_deck()
    joueur = Joueur("Joueur 1")
    croupier = Croupier()

    # Distribuer les cartes initiales (2 pour chacun)
    for _ in range(2):
        joueur.ajouter_carte(deck.pop())
        croupier.ajouter_carte(deck.pop())

    # Affichage de la première carte du joueur
    premiere_carte_joueur : Cartes = joueur.main[0]
    afficherCarte(premiere_carte_joueur)
    pg.carte_joueur(1, chiffre, couleur, symbole)

    #Affichage de la deuxième carte du joueur
    deuxieme_carte_joueur : Cartes = joueur.main[1]
    afficherCarte(deuxieme_carte_joueur)
    pg.carte_joueur(2, chiffre, couleur, symbole)

    # Tour du joueur
    tour_joueur(joueur, deck)

    # Affichage de la première carte du croupier
    # Récupérer la première carte
    premiere_carte_croupier : Cartes = croupier.main[0]
    afficherCarte(premiere_carte_croupier)
    pg.carte_dealer(1, chiffre, couleur, symbole)

    # Tour du croupier
    #tour_croupier(croupier, deck)

    # Affichage de la 2e carte du croupier
    deuxieme_carte_croupier : Cartes = croupier.main[1]
    afficherCarte(deuxieme_carte_croupier)
    pg.carte_dealer(2, chiffre, couleur, symbole)
