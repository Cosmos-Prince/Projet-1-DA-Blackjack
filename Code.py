#%%
import random

#cartes
Synbole_Cartes= ['coeur', 'Diamant', 'trefle', 'Pique'] 
liste_Carte= ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = [(card, category) for category in Synbole_Cartes for card in liste_Carte]

#Mise en valeur des cartes 
def valeur_cartes(carte):
    if carte[0] in ['J' , 'Q ', 'K']:
        return 10
    elif carte[0] == 'A':
        return 11
    else:
        return int(carte[0])
#Mélange des cartes avec .pop pour pas réutiliser les cartes
random.shuffle(deck)
carte_joueur = [deck.pop() , deck.pop()]
carte_croupier = [deck.pop() , deck.pop()]
#Calcul de la valeur des carte pour le croupier et joueur
#Calcul du score du joueur et croupier et début du code pour déternminer le gagnant
while True:
    score_joueur = sum(valeur_cartes(carte) for carte in carte_joueur)
    score_croupier = sum(valeur_cartes(carte) for carte in carte_croupier)
    print("Carte au joueur:", carte_joueur)
    print("Carte_croupier:", carte_croupier)
    print("\n")
    Choix = input(' "jouer" pour continuer, "stop" pour arreter]:').lower()
    if Choix == "jouer":
        nouvelle_cartes = deck.pop()
        carte_joueur.append(nouvelle_cartes)
    elif Choix == "stop":
        break
    else:
        print("Choix invalide, veuillez réessayer")
        continue

    if score_joueur > 21:
        print("Cartes du croupier", carte_croupier)
        print("Score du croupier", score_croupier)
        print("Cartes du jouer:", carte_joueur)
        print("Score du jouer:", score_joueur)
        print("Croupier gagnant (valeurs des cartes > 21:)")
        break
    #après le tour de joueur, calcul du score pour le scroupier pour voir s'il est > 17 sinon on ajoute des cartes
    if score_croupier < 17:
        nouvelle_cartes = deck.pop()
        carte_croupier.append(nouvelle_cartes)
        score_croupier += valeur_cartes(nouvelle_cartes)

    





# %%
