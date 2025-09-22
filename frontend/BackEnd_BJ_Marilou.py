##################################################################################################
# CRÉATION DE LA CLASSE CARTES
#=============================

# Le module random est importé pour mélanger le deck
import random
import tkinter as tk
import page_de_jeu as pg

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

def creer_deck():
        # Rassemble toutes les cartes déjà créées
        toutes_les_cartes = [
            HA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK,
            DA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK,
            SA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK,
            CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK
        ]
        toutes_les_cartes = toutes_les_cartes[:]  # copie de la liste
        random.shuffle(toutes_les_cartes)
        return toutes_les_cartes

##################################################################################################


##################################################################################################################
# CRÉATION DE LA CLASSE ACTEUR (CLASSES FILLES JOUEUR ET CROUPIER)
#=================================================================

class Acteur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    # Méthode pour ajouter une carte à la main
    def ajouter_carte(self, carte):
        self.main.append(carte)

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

#############################################################################################################
# FONCTION POUR DEMANDER LE NOMBRE DE JOUEURS (1-3) --> À MODIFIER DANS TKINTER (PAS D'INPUT/PRINT)
#==================================================================================================

#def demander_nb_joueurs():
#    while True:
#        try:
#            nb = int(input("Combien de joueur (1-3)? "))
#            if 1 <= nb <= 3:
#                return nb
#            else:
#                print("Veuillez entrer un nombre entre 1 et 3.")
#        except ValueError:
#            print("Entrée invalide : Veuillez entrer un nombre entier.")



##############################################################################################################
# FONCTION POUR CALCULER LE SCORE D'UNE MAIN
#===========================================

# Calcul du score
def calculer_score(main):
    total = sum(carte.getValeur() for carte in main)
    nb_as = sum(1 for carte in main if carte.getSymbole() == "A")
    # Convertir des As de 11 à 1 tant que ça dépasse 21
    while total > 21 and nb_as > 0:
        total -= 10
        nb_as -= 1
    return total

##############################################################################################################
# GESTION DU JEU (TOURS DES JOUEURS ET DU CROUPIER)
#==================================================

# Fonction pour gérer les tours des joueur
def tour_joueur(joueur, deck):
    # Tour d'un joueur à la fois
    while calculer_score(joueur.main) < 21:
        #print(f"\nMain de {joueur.nom}: {joueur.afficher_main()} (Score: {calculer_score(joueur.main)})")
        action = pg.choix_joueur.get()
        if action == "tirer":
            # Fonction pop() pour retirer du deck la carte piochée
            joueur.ajouter_carte(deck.pop())

            # Affichage de la carte piochée
            carte_piochée : Cartes = joueur.main[-1]
            chiffre = carte_piochée.getChiffre()
            symbole = carte_piochée.getSymboleAffichage()
            couleur = carte_piochée.getCouleur()
            chiffre_var = tk.StringVar()
            symbole_var = tk.StringVar()
            couleur_var = tk.StringVar()
            chiffre_var.set(chiffre)
            symbole_var.set(symbole)
            couleur_var.set(couleur)

            pg.carte_joueur(len(joueur.main), chiffre, couleur, symbole)
        else:
            break
    
    

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
    # Création du deck
    deck = creer_deck()
    # Création du joueur unique
    joueur = Joueur("Joueur 1")

    # Création du croupier
    croupier = Croupier()

    # Distribuer les cartes initiales (2 pour chacun)
    for _ in range(2):
        joueur.ajouter_carte(deck.pop())
        croupier.ajouter_carte(deck.pop())

    # Affichage de la première carte du joueur
    premiere_carte_joueur : Cartes = joueur.main[0]

    # Récupérer le chiffre et le symbole
    chiffre = premiere_carte_joueur.getChiffre()
    symbole = premiere_carte_joueur.getSymboleAffichage()
    couleur = premiere_carte_joueur.getCouleur()

    # Mettre dans des variables Tkinter
    chiffre_var = tk.StringVar()
    symbole_var = tk.StringVar()
    couleur_var = tk.StringVar()
    chiffre_var.set(chiffre)
    symbole_var.set(symbole)
    couleur_var.set(couleur)

    pg.carte_joueur(1, chiffre, couleur, symbole)

    #Affichage de la deuxième carte du joueur
    deuxieme_carte_joueur : Cartes = joueur.main[1]

    # Récupérer le chiffre et le symbole
    chiffre = deuxieme_carte_joueur.getChiffre()
    symbole = deuxieme_carte_joueur.getSymboleAffichage()
    couleur = deuxieme_carte_joueur.getCouleur()

    # Mettre dans des variables Tkinter
    chiffre_var = tk.StringVar()
    symbole_var = tk.StringVar()
    couleur_var = tk.StringVar()
    chiffre_var.set(chiffre)
    symbole_var.set(symbole)
    couleur_var.set(couleur)

    pg.carte_joueur(2, chiffre, couleur, symbole)




    # Tour du joueur
    tour_joueur(joueur, deck)

    # Affichage de la première carte du croupier
    # Récupérer la première carte
    premiere_carte_croupier : Cartes = croupier.main[0]

    # Récupérer le chiffre et le symbole
    chiffre = premiere_carte_croupier.getChiffre()
    symbole = premiere_carte_croupier.getSymboleAffichage()
    couleur = premiere_carte_croupier.getCouleur()

    # Mettre dans des variables Tkinter
    chiffre_var = tk.StringVar()
    symbole_var = tk.StringVar()
    couleur_var = tk.StringVar()
    chiffre_var.set(chiffre)
    symbole_var.set(symbole)
    couleur_var.set(couleur)

    pg.carte_dealer(1, chiffre, couleur, symbole)

    # Tour du croupier
    #tour_croupier(croupier, deck)

    # Affichage de la 2e carte du croupier
    deuxieme_carte_croupier : Cartes = croupier.main[1]

    # Récupérer le chiffre et le symbole
    chiffre = deuxieme_carte_croupier.getChiffre()
    symbole = deuxieme_carte_croupier.getSymboleAffichage()
    couleur = deuxieme_carte_croupier.getCouleur()

    # Mettre dans des variables Tkinter
    chiffre2_var = tk.StringVar()
    symbole2_var = tk.StringVar()
    couleur2_var = tk.StringVar()
    chiffre2_var.set(chiffre)
    symbole2_var.set(symbole)
    couleur2_var.set(couleur)

    pg.carte_dealer(2, chiffre, couleur, symbole)

    # Résultats
    #print("\n*** RÉSULTATS ***")
    #score_croupier = calculer_score(croupier.main)
    #score_joueur = calculer_score(joueur.main)
    #if score_joueur > 21:
    #    verdict = "perdu (bust)"
    #elif score_croupier > 21 or score_joueur > score_croupier:
    #    verdict = "gagné"
    #elif score_joueur < score_croupier:
    #    verdict = "perdu"
    #else:
    #    verdict = "égalité (push)"
    #print(f"{joueur.nom}: {joueur.afficher_main()} --> {score_joueur} | {verdict}")



    deuxieme_carte_croupier : Cartes = croupier.main[1]

    # Récupérer le chiffre et le symbole
    chiffre = deuxieme_carte_croupier.getChiffre()
    symbole = deuxieme_carte_croupier.getSymboleAffichage()
    couleur = deuxieme_carte_croupier.getCouleur()

    # Mettre dans des variables Tkinter
    chiffre2_var = tk.StringVar()
    symbole2_var = tk.StringVar()
    couleur2_var = tk.StringVar()
    chiffre2_var.set(chiffre)
    symbole2_var.set(symbole)
    couleur2_var.set(couleur)

    pg.carte_dealer(2, chiffre, couleur, symbole)

if __name__ == "__main__":
    # Mainloop de la fenêtre Tkinter
    gerer_les_tours()
    pg.fenetre.mainloop()

    # Affichage de la première carte du joueur
    # print(joueur.afficher_premier_carte())  # joueur est maintenant local à gerer_les_tours

