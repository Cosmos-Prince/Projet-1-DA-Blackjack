class Cartes:
    # Constructeur pour les cartes, le chiffre est un str puisqu'il doit accepter J Q K
    def __init__(self, chiffre: str, symbole: str):
        self.__chiffre: str = chiffre
        self.__symbole: str = symbole


    # Getter pour retourner la valeur de la carte (les figures valent 10)
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
    
    def getSymbole(self):
        return self.__symbole
    
    def getCouleur(self):
        if self.__symbole in ("Coeur", "Carreau"):
            return "red"
        else:
            return "black"
    
    def getSymboleAffichage(self):
        symboles_affichage = {
            "Coeur": "♥",
            "Carreau": "♦",
            "Pique": "♠",
            "Trefle": "♣"
        }
        return symboles_affichage.get(self.__symbole, "")


    # Affichage pour représenter une carte
    def __repr__(self):
        return f"{self.__chiffre} de {self.__symbole}"


# Initialisation de toutes les cartes

# Cartes de Coeur
HA = Cartes("A", "Coeur")
H2 = Cartes("2", "Coeur")
H3 = Cartes("3", "Coeur")
H4 = Cartes("4", "Coeur")
H5 = Cartes("5", "Coeur")
H6 = Cartes("6", "Coeur")
H7 = Cartes("7", "Coeur")
H8 = Cartes("8", "Coeur")
H9 = Cartes("9", "Coeur")
H10 = Cartes("10", "Coeur")
HJ = Cartes("J", "Coeur")
HQ = Cartes("Q", "Coeur")
HK = Cartes("K", "Coeur")

# Cartes de Carreau
DA = Cartes("A", "Carreau")
D2 = Cartes("2", "Carreau")
D3 = Cartes("3", "Carreau")
D4 = Cartes("4", "Carreau")
D5 = Cartes("5", "Carreau")
D6 = Cartes("6", "Carreau")
D7 = Cartes("7", "Carreau")
D8 = Cartes("8", "Carreau")
D9 = Cartes("9", "Carreau")
D10 = Cartes("10", "Carreau")
DJ = Cartes("J", "Carreau")
DQ = Cartes("Q", "Carreau")
DK = Cartes("K", "Carreau")

# Cartes de Pique
SA = Cartes("A", "Pique")
S2 = Cartes("2", "Pique")
S3 = Cartes("3", "Pique")
S4 = Cartes("4", "Pique")
S5 = Cartes("5", "Pique")
S6 = Cartes("6", "Pique")
S7 = Cartes("7", "Pique")
S8 = Cartes("8", "Pique")
S9 = Cartes("9", "Pique")
S10 = Cartes("10", "Pique")
SJ = Cartes("J", "Pique")
SQ = Cartes("Q", "Pique")
SK = Cartes("K", "Pique")

# Cartes de Trèfle
CA = Cartes("A", "Trefle")
C2 = Cartes("2", "Trefle")
C3 = Cartes("3", "Trefle")
C4 = Cartes("4", "Trefle")
C5 = Cartes("5", "Trefle")
C6 = Cartes("6", "Trefle")
C7 = Cartes("7", "Trefle")
C8 = Cartes("8", "Trefle")
C9 = Cartes("9", "Trefle")
C10 = Cartes("10", "Trefle")
CJ = Cartes("J", "Trefle")
CQ = Cartes("Q", "Trefle")
CK = Cartes("K", "Trefle")
