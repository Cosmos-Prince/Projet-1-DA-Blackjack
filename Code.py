import random
#cartes
Synbole_Cartes= ['coeur', 'Diamant', 'trefle', 'Pique'] 
liste_Carte= ['A', '2', '3', '4', '5', '6','7','8','9', '10', 'J', 'Q', 'K']
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
carte_jouer = [deck.pop() , deck.pop()]
carte_croupier = [deck.pop() , deck.pop()]
#Calcul de la valeur des carte pour le croupier et joueur
while True:
    score_jouer = sum(carte_jouer(carte) for carte in carte_jouer)
    carte_croupier = sum(carte_jouer(carte) for carte in carte_croupier)


