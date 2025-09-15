# Import de plusieurs modules nécessaires pour le fonctionnement (cards.py, score.py et acteurs.py)
from score import calculer_score
from acteurs import Joueur
import cards   

# Fonction pour gérer le tour du joueur
def tour_joueur(joueur, deck):
    while calculer_score(joueur.main) < 21:
        print(f"\nMain de {joueur.nom}: {joueur.afficher_main()} (Score: {calculer_score(joueur.main)})")
        action = joueur.choisir_action()
        if action == "tirer":
            joueur.ajouter_carte(deck.pop())
        else:
            break


# Exemple pour tester (avec if __name__ == "__main__": pour ne pas déclencher le fichier ailleurs)
if __name__ == "__main__":
    # Création du deck et des joueurs
    deck = cards.Cartes.creer_deck()
    joueur1 = Joueur("DaGambler")
    # Ajouter des cartes initiales pour tester
    joueur1.ajouter_carte(deck.pop())
    joueur1.ajouter_carte(deck.pop())
    tour_joueur(joueur1, deck)





