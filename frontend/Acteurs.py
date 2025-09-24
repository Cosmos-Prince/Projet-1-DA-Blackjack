from Cartes import *

##################################################################################################################
# CRÉATION DE LA CLASSE ACTEUR (CLASSES FILLES JOUEUR ET CROUPIER)
#=================================================================

class Acteur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        self.__score = 0


    # Méthode pour ajouter une carte à la main
    def ajouter_carte(self, carte):
        self.main.append(carte)
        self.calculer_score()


    def getScore(self):
        return self.__score


    # Calcul du score
    def calculer_score(self):
        total = sum(carte.getValeur() for carte in self.main)
        nb_as = sum(1 for carte in self.main if carte.getSymbole() == "A")
        # Convertir des As de 11 à 1 tant que ça dépasse 21
        while total > 21 and nb_as > 0:
            total -= 10
            nb_as -= 1

        self.__score = total


    # Méthode pour afficher le nom de l'acteur
    def __str__(self):
        return self.nom
    


class Joueur(Acteur):
    def __init__(self, nom):
        super().__init__(nom)


    def afficher_premier_carte(self):
        if self.main:
            return str(self.main[0])
        return "Aucune carte"
    

    def afficher_deuxieme_carte(self):
        if len(self.main) > 1:
            return str(self.main[1])
        return "Aucune carte"


    # Méthode pour afficher la main du joueur
    def afficher_main(self):
        return ', '.join(str(carte) for carte in self.main)


class Croupier(Acteur):
    def __init__(self):
        super().__init__("Croupier")


    # Méthode pour afficher la main du croupier
    def afficher_main(self, reveal=False):
        # reveal=True montre toutes les cartes
        if reveal:
            return ', '.join(str(carte) for carte in self.main)
        else:
            # reveal=False garde la 2e carte cachée
            if not self.main:
                return "Aucune carte"
            return f"{self.main[0]}, Carte cachée"
