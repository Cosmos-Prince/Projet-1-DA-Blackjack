# Le module random est importé pour mélanger le deck
import random


class Cartes():
    # Constructeur pour les cartes, le chiffre est un str puisqu'il doit accepter J Q K
    def __init__(self, chiffre:str, couleur:str):
        self.__chiffre:str = chiffre
        self.__couleur:str = couleur
    
    # Getter pour retourner la valeur de la carte dans le jeu, les figures valent 10 donc on retourne 10
    def getValeur(self):
        if self.__chiffre in ("J", "Q", "K"):
            return 10
        elif self.__chiffre == "A":
            return 11
        else:
            return int(self.__chiffre)
    
    # Getters pour l'affichage
    def getChiffre(self):
        return self.__chiffre
        
    def getCouleur(self):
        return self.__couleur
    
     # Affichage pour représenter le deck (sert pour tester si le programme fonnctionne)
    def __repr__(self):
        return f"{self.__chiffre} de {self.__couleur}"
    
    # Création d'un deck de 52 cartes
    @staticmethod
    def creer_deck():
        # Rassemble toutes les cartes déjà créées
        toutes_les_cartes = [
            HA,H2,H3,H4,H5,H6,H7,H8,H9,H10,HJ,HQ,HK,
            DA,D2,D3,D4,D5,D6,D7,D8,D9,D10,DJ,DQ,DK,
            SA,S2,S3,S4,S5,S6,S7,S8,S9,S10,SJ,SQ,SK,
            CA,C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK
        ]
        random.shuffle(toutes_les_cartes)
        return toutes_les_cartes


# Initialisation de toutes les cartes

# Cartes de Coeur
HA:Cartes = Cartes("A", "Coeur")
H2:Cartes = Cartes("2", "Coeur")
H3:Cartes = Cartes("3", "Coeur")
H4:Cartes = Cartes("4", "Coeur")
H5:Cartes = Cartes("5", "Coeur")
H6:Cartes = Cartes("6", "Coeur")
H7:Cartes = Cartes("7", "Coeur")
H8:Cartes = Cartes("8", "Coeur")
H9:Cartes = Cartes("9", "Coeur")
H10:Cartes = Cartes("10", "Coeur")
HJ:Cartes = Cartes("J", "Coeur")
HQ:Cartes = Cartes("Q", "Coeur")
HK:Cartes = Cartes("K", "Coeur")
    
# Cartes de Carreau
DA:Cartes = Cartes("A", "Carreau")
D2:Cartes = Cartes("2", "Carreau")
D3:Cartes = Cartes("3", "Carreau")
D4:Cartes = Cartes("4", "Carreau")
D5:Cartes = Cartes("5", "Carreau")
D6:Cartes = Cartes("6", "Carreau")
D7:Cartes = Cartes("7", "Carreau")
D8:Cartes = Cartes("8", "Carreau")
D9:Cartes = Cartes("9", "Carreau")
D10:Cartes = Cartes("10", "Carreau")
DJ:Cartes = Cartes("J", "Carreau")
DQ:Cartes = Cartes("Q", "Carreau")
DK:Cartes = Cartes("K", "Carreau")

# Cartes de Pique
SA:Cartes = Cartes("A", "Pique")
S2:Cartes = Cartes("2", "Pique")
S3:Cartes = Cartes("3", "Pique")
S4:Cartes = Cartes("4", "Pique")
S5:Cartes = Cartes("5", "Pique")
S6:Cartes = Cartes("6", "Pique")
S7:Cartes = Cartes("7", "Pique")
S8:Cartes = Cartes("8", "Pique")
S9:Cartes = Cartes("9", "Pique")
S10:Cartes = Cartes("10", "Pique")
SJ:Cartes = Cartes("J", "Pique")
SQ:Cartes = Cartes("Q", "Pique")
SK:Cartes = Cartes("K", "Pique")

# Cartes Trèfle
CA:Cartes = Cartes("A", "Trefle")
C2:Cartes = Cartes("2", "Trefle")
C3:Cartes = Cartes("3", "Trefle")
C4:Cartes = Cartes("4", "Trefle")
C5:Cartes = Cartes("5", "Trefle")
C6:Cartes = Cartes("6", "Trefle")
C7:Cartes = Cartes("7", "Trefle")
C8:Cartes = Cartes("8", "Trefle")
C9:Cartes = Cartes("9", "Trefle")
C10:Cartes = Cartes("10", "Trefle")
CJ:Cartes = Cartes("J", "Trefle")
CQ:Cartes = Cartes("Q", "Trefle")
CK:Cartes = Cartes("K", "Trefle")


# Test pour voir si le deck est bien créé
# if __name__ == "__main__" empêche l'exécution du code lors de l'importation du module dans un autre 
# fichier
if __name__ == "__main__":
    deck = Cartes.creer_deck()
    print(deck)

