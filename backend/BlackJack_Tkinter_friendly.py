##################################################################################################
# CRÉATION DE LA CLASSE CARTES
#=============================

import random

class Cartes:
    # Constructeur pour les cartes, le chiffre est un str puisqu'il doit accepter J Q K
    def __init__(self, chiffre: str, couleur: str):
        self.__chiffre: str = chiffre
        self.__couleur: str = couleur

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

    def getCouleur(self):
        return self.__couleur

    # Affichage pour représenter une carte
    def __repr__(self):
        return f"{self.__chiffre} de {self.__couleur}"

    # Création d'un deck de 52 cartes (statique)
    @staticmethod
    def creer_deck():
        toutes_les_cartes = [
            HA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK,
            DA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK,
            SA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK,
            CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK
        ]
        toutes_les_cartes = toutes_les_cartes[:]  # copie de la liste
        random.shuffle(toutes_les_cartes)
        return toutes_les_cartes


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

    # Méthode pour choisir une action : injectée (GUI) ou console
    # - input_action_func: callable(joueur: Joueur, score_actuel: int) -> str ("tirer" ou "rester")
    def choisir_action(self, score_actuel, input_action_func=None, output_func=print):
        if input_action_func is None:
            # Mode console (comportement original)
            while True:
                action = input(f"{self.nom}, 'tirer' une carte ou 'rester'? ").lower()
                if action in ['tirer', 'rester']:
                    return action
                else:
                    output_func("Action invalide: 'tirer' ou 'rester'.")
        else:
            # Mode GUI (ou autre) via callback
            action = input_action_func(self, score_actuel)
            return action

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
# FONCTION POUR DEMANDER LE NOMBRE DE JOUEURS
#  - input_nb_joueurs_func: callable() -> int (1..3) ; si None, mode console.
#==================================================================================================

def demander_nb_joueurs(input_nb_joueurs_func=None, output_func=print):
    if input_nb_joueurs_func is not None:
        nb = int(input_nb_joueurs_func())
        return max(1, min(3, nb))
    while True:
        try:
            nb = int(input("Combien de joueurs (1-3)? "))
            if 1 <= nb <= 3:
                return nb
            else:
                output_func("Veuillez entrer un nombre entre 1 et 3.")
        except ValueError:
            output_func("Entrée invalide : Veuillez entrer un nombre entier.")


##############################################################################################################
# FONCTION POUR CALCULER LE SCORE D'UNE MAIN
#===========================================

def calculer_score(main):
    total = sum(carte.getValeur() for carte in main)
    nb_as = sum(1 for carte in main if carte.getChiffre() == "A")
    # Convertir des As de 11 à 1 tant que ça dépasse 21
    while total > 21 and nb_as > 0:
        total -= 10
        nb_as -= 1
    return total

##############################################################################################################
# GESTION DU JEU (TOURS DES JOUEURS ET DU CROUPIER)
#==================================================

def tour_joueur(joueur, deck, input_action_func=None, output_func=print):
    # Tour d'un joueur à la fois
    while calculer_score(joueur.main) < 21:
        score = calculer_score(joueur.main)
        output_func(f"\nMain de {joueur.nom}: {joueur.afficher_main()} (Score: {score})")
        action = joueur.choisir_action(score, input_action_func=input_action_func, output_func=output_func)
        if action == "tirer":
            joueur.ajouter_carte(deck.pop())
        else:
            break

def tour_croupier(croupier, deck, output_func=print):
    output_func(f"\nMain du croupier (cachée): {croupier.afficher_main(reveal=False)}")
    while calculer_score(croupier.main) < 17:
        croupier.ajouter_carte(deck.pop())
        output_func(f"Croupier tire et obtient (Score: {calculer_score(croupier.main)})")
    output_func(f"Main du croupier (révélée): {croupier.afficher_main(reveal=True)} "
                f"(Score: {calculer_score(croupier.main)})")

def gerer_les_tours(input_nb_joueurs_func=None, input_action_func=None, output_func=print):
    deck = Cartes.creer_deck()
    nb = demander_nb_joueurs(input_nb_joueurs_func=input_nb_joueurs_func, output_func=output_func)
    joueurs = [Joueur(f"Joueur {i+1}") for i in range(nb)]
    croupier = Croupier()

    # Distribuer les cartes initiales (2 pour chacun)
    for _ in range(2):
        for joueur in joueurs:
            joueur.ajouter_carte(deck.pop())
        croupier.ajouter_carte(deck.pop())

    # Afficher les mains initiales
    output_func("\n*** MAINS INITIALES ***")
    for joueur in joueurs:
        output_func(f"{joueur.nom}: {joueur.afficher_main()} (Score: {calculer_score(joueur.main)})")
    output_func(f"Croupier: {croupier.afficher_main(reveal=False)}")

    # Tours des joueurs
    for joueur in joueurs:
        tour_joueur(joueur, deck, input_action_func=input_action_func, output_func=output_func)

    # Tour du croupier
    tour_croupier(croupier, deck, output_func=output_func)

    # Résultats
    output_func("\n*** RÉSULTATS ***")
    score_croupier = calculer_score(croupier.main)
    for joueur in joueurs:
        score_joueur = calculer_score(joueur.main)
        if score_joueur > 21:
            verdict = "perdu (bust)"
        elif score_croupier > 21 or score_joueur > score_croupier:
            verdict = "gagné"
        elif score_joueur < score_croupier:
            verdict = "perdu"
        else:
            verdict = "égalité (push)"
        output_func(f"{joueur.nom}: {joueur.afficher_main()} --> {score_joueur} | {verdict}")

##############################################################################################
# FONCTION QUI RETOURNE LA PREMIÈRE CARTE DU JOUEUR
def get_premiere_carte(joueur: Joueur):
    if joueur.main:
        return joueur.main[0]
    return None

##############################################################################################################
# FRONT-END TKINTER MINIMAL (optionnel)
# - utilise simpledialog pour les entrées et un Text pour l'affichage
#==========================

if __name__ == "__main__":
    try:
        import tkinter as tk
        from tkinter import simpledialog, messagebox

        class BlackjackApp(tk.Tk):
            def __init__(self):
                super().__init__()
                self.title("Black Jack (GUI minimal)")
                self.geometry("700x500")

                self.txt = tk.Text(self, wrap="word")
                self.txt.pack(fill="both", expand=True)

                self.btn_frame = tk.Frame(self)
                self.btn_frame.pack(fill="x")

                self.btn_start = tk.Button(self.btn_frame, text="Démarrer une partie", command=self.start_game)
                self.btn_start.pack(side="left", padx=5, pady=5)

                # variable où l’action choisie sera déposée par askstring
                self._last_action = None

            def gui_log(self, msg):
                self.txt.insert("end", msg + "\n")
                self.txt.see("end")
                self.update_idletasks()

            def ask_nb_joueurs(self):
                nb = simpledialog.askinteger("Joueurs", "Combien de joueurs (1-3) ?", minvalue=1, maxvalue=3, parent=self)
                if nb is None:
                    # Annulation -> par défaut 1
                    nb = 1
                return nb

            def ask_action(self, joueur: Joueur, score_actuel: int):
                # Dialogue modal: l’utilisateur tape 'tirer' ou 'rester'
                while True:
                    action = simpledialog.askstring(
                        "Action",
                        f"{joueur.nom} (score {score_actuel}) : taper 'tirer' ou 'rester'",
                        parent=self
                    )
                    if action is None:
                        # Si annule, on considère 'rester'
                        return "rester"
                    action = action.strip().lower()
                    if action in ("tirer", "rester"):
                        return action
                    messagebox.showinfo("Info", "Veuillez entrer 'tirer' ou 'rester'.")

            def start_game(self):
                self.txt.delete("1.0", "end")
                try:
                    gerer_les_tours(
                        input_nb_joueurs_func=self.ask_nb_joueurs,
                        input_action_func=self.ask_action,
                        output_func=self.gui_log
                    )
                except Exception as e:
                    messagebox.showerror("Erreur", str(e))

        app = BlackjackApp()
        app.mainloop()

    except Exception:
        # Si Tkinter n’est pas dispo ou si on veut rester en console, on garde le comportement original.
        gerer_les_tours()

def demarrer_jeu():
    if __name__ == "__main__":
        gerer_les_tours()