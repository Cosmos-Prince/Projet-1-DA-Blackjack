# Importer le module cards pour accéder aux cartes (deck et Cartes)
import cards


# Créer une classe Acteur
class Acteur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    # Méthode pour ajouter une carte à la main de l'acteur
    def ajouter_carte(self, carte):
        self.main.append(carte)

    # Méthode pour afficher le nom de l'acteur
    def __str__(self):
        return self.nom
    

# Créer une classe Joueur qui hérite de Acteurs
class Joueur(Acteur):
    def __init__(self, nom):
        super().__init__(nom)

    # Méthode pour choisir une action
    def choisir_action(self):
        while True:
            action = input(f"{self.nom}, voulez-vous 'tirer' une carte ou 'rester'? ").lower()
            if action in ['tirer', 'rester']:
                return action
            else:
                print("Action invalide. Veuillez entrer 'tirer' ou 'rester'.")

    # Méthode pour afficher la main du joueur       
    def afficher_main(self):
        return ', '.join(str(carte) for carte in self.main)
     

# Créer une classe Croupier qui hérite de Acteur
class Croupier(Acteur):
    def __init__(self):
        super().__init__("Croupier")

    # Méthode pour afficher la main du croupier et cacher une carte
    def afficher_main(self, reveal=False):
        if reveal:
            # Si reveal=True cela affiche toutes les cartes
            return ', '.join(str(carte) for carte in self.main)
        else:
            # Si reveal=False cela affiche la première carte et la carte cachée
            return f"{self.main[0]}, Carte cachée"
        

# Exemple pour tester les classes

# if __name__ == "__main__" empêche l'exécution du code lors de l'importation du module dans un autre
# fichier
if __name__ == "__main__": 
    joueur1 = Joueur("DaGambler")
    croupier = Croupier()
    
    # Ajouter des cartes pour tester
    joueur1.ajouter_carte(cards.deck.pop())
    joueur1.ajouter_carte(cards.deck.pop())
    croupier.ajouter_carte(cards.deck.pop())
    croupier.ajouter_carte(cards.deck.pop())

    # Afficher les mains
    print(joueur1.afficher_main())
    print(croupier.afficher_main())
    print(croupier.afficher_main(reveal=True))

    # Exemple d'utilisation de la classe Joueur
    action = joueur1.choisir_action()
    print(f"{joueur1.nom} a choisi de {action}.")