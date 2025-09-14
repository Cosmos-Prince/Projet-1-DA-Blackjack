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
carte_joueur = [deck.pop() , deck.pop()]
carte_croupier = [deck.pop() , deck.pop()]
#Calcul de la valeur des carte pour le croupier et joueur

while True:
    score_joueur = sum(valeur_cartes(carte) for carte in carte_joueur)
    carte_croupier = sum(valeur_cartes(carte) for carte in carte_croupier)
    print("Carte au joueur:", score_joueur)
    print("Carte_croupier:", carte_croupier)
    print("\n")
    choice = input('What do you want? ["play" to resquest another card, "stop" to stop]:').lower()
    if choice == "play":
        new_card = deck.pop()
        score_joueur.append(new_card)
    elif choice == "stop":
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    if score_joueur > 21:
        print("Cards Dealer Has:", carte_croupier)
        print("S")





# %%
