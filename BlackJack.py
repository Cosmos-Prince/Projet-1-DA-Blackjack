import tkinter as tk
from affichageCartes import *
from fonctions import *
from Cartes import *
from Acteurs import *

class BlackJack(tk.Toplevel): 
    def __init__(self, master=None):
        super().__init__(master)

        self.deck:list = creer_deck()
        self.Player1:Joueur = Joueur("Joueur 1")
        self.Dealer:Croupier = Croupier()
        self.dealer_carte_cachee = None  # Variable pour stocker la carte face cachée du dealer
        self.scoreTotalDealer = 0
        self.scoreTotalJoueur = 0
        #Création des instances pour la partie, elles sont utilisées dans plusieurs fonctions à l'aide de global

        # Titre de la fenêtre
        self.title("Black Jack")
        # Taille de la fenêtre
        largeur= self.winfo_screenwidth()               
        hauteur= self.winfo_screenheight()
        self.geometry("%dx%d" %(largeur, hauteur))

        '''
        =====================================
        PLACEMENT DES FRAMES, BACKGROUND, ETC
        =====================================
        '''

        # Définir la couleur de fond en vert
        self.configure(bg="#085b18")

        # Création d'une première Frame qui va faire la bordure
        self.frameBordure = tk.Frame(self, bg="#5d5103", width=(largeur - 100), height=(hauteur - 150))
        self.frameBordure.place(x=50, y=50)

        # Création du frame principal pour le jeu
        self.frameJeu = tk.Frame(self.frameBordure, bg="#0b7821", width=(largeur - 150), height=(hauteur - 200))
        self.frameJeu.place(x=25, y=25)

        # Création du frame du titre
        self.frameTitre = tk.Frame(self.frameJeu, bg="#0b7821", padx=20, pady=20, height=100, width=(largeur - 150))
        self.frameTitre.place(x=0, y=0)

        # Ajouter un titre dans le haut
        self.titre_label = tk.Label(self.frameTitre, text="Black Jack", font=("Algerian", 24),bg="#0b7821", fg="#7cff85")
        self.titre_label.place(relx=0.5, rely=0.2, anchor="center")  # Centré en haut

        # Création d'une frame pour le dealer
        self.frameDealer = tk.Frame(self.frameJeu, bg="#0b7821", height=400, width=(largeur - 150))
        self.frameDealer.place(x=0, y=50)

        # Création d'une frame pour le joueur
        self.frameJoueur = tk.Frame(self.frameJeu, bg="#0b7821", height=400, width=(largeur - 150))
        self.frameJoueur.place(x=0, y=525)

        # Frame pour afficher le score du joueur
        self.frameScoreMainJoueur = tk.Frame(self.frameJoueur, bg="#0b7821", padx=20, pady=20, height=400, width=250)
        self.frameScoreMainJoueur.place(relx=0.87, y=0)

        # Label pour afficher le score de la main du joueur
        self.scoreMainJoueurLabel = tk.Label(self.frameScoreMainJoueur, text=f"Score: {self.Player1.getScore()}", font=("Arial", 16), bg="#0b7821", fg="white")
        self.scoreMainJoueurLabel.place(relx=0.5, rely=0.5, anchor="center")

        # Frame pour les cartes du joueur
        self.frameCartesJoueur = tk.Frame(self.frameJoueur, bg="#0b7821", padx=20, pady=20, height=400, width=500)
        self.frameCartesJoueur.place(relx=0.36, y=0)  # Centré horizontalement

        # Frame pour afficher le total des victoires du dealer & du joueur
        self.frameScoreTotal = tk.Frame(self.frameDealer, bg="#0b7821", padx=20, pady=20, height=400, width=400)
        self.frameScoreTotal.place(relx=0, y=0)  # <-- Modifié pour être plus à gauche

        # Label pour afficher le score total du dealer
        self.scoreTotalDealerLabel = tk.Label(self.frameScoreTotal, text="Victoires totales Dealer: 0", font=("Arial", 16), bg="#0b7821", fg="white")
        self.scoreTotalDealerLabel.place(relx=0.5, rely=0.3, anchor="center")  # Centré

        # Label pour afficher le score total du joueur
        self.scoreTotalJoueurLabel = tk.Label(self.frameScoreTotal, text="Victoires totales Joueur: 0", font=("Arial", 16), bg="#0b7821", fg="white")
        self.scoreTotalJoueurLabel.place(relx=0.5, rely=0.7, anchor="center")  # Centré

        # Frame pour les cartes du dealer
        self.frameCartesDealer = tk.Frame(self.frameDealer, bg="#0b7821", padx=20, pady=20, height=400, width=500)
        self.frameCartesDealer.place(relx=0.36, y=0)  # Centré horizontalement

        # Label pour indiquer le tour au joueur
        self.tour_label = tk.Label(self.frameJeu, text="À votre tour : Tirer ou rester", font=("Arial", 20), bg="#0b7821", fg="#ffffff")
        self.tour_label.place(relx=0.75, y=75, anchor="center")  # Centré horizontalement

        '''
        =====================================
        FRAMES POUR LES BOUTTONS
        =====================================
        '''

        # Création d'une frame pour les boutons
        self.frameBoutons = tk.Frame(self.frameJeu, bg="#0b7821", height=100, width=(largeur - 150))
        self.frameBoutons.place(x=0, y=400)   # entre dealer et joueur

        # Création du bouton tirer une carte (dans frameBoutons)
        self.bouton_tirer = tk.Button(self.frameBoutons, text="Tirer", font=("Arial", 16), bg="#4CAF50", fg="white", padx=10, pady=5, command=self.choisir_tirer)
        self.bouton_tirer.place(relx=0.38, rely=0.5, anchor="center")
          # Centré verticalement et à gauche

        # Création du bouton rester (dans frameBoutons)
        self.bouton_rester = tk.Button(self.frameBoutons, text="Rester", font=("Arial", 16), bg="#f44336", fg="white", padx=10, pady=5, command=self.choisir_rester)
        self.bouton_rester.place(relx=0.52, rely=0.5, anchor="center")

        # Création du bouton nouvelle partie (dans frameBoutons)
        self.bouton_nouvelle_partie = tk.Button(self.frameBoutons,text="Nouvelle partie",font=("Arial", 16),bg="#2196F3",fg="white",padx=10,pady=5,command=self.nouvelle_partie)
        self.bouton_nouvelle_partie.place(relx=0.66, rely=0.5, anchor="center")


    # Logique lorsque le boutton "hit" est appuyé
    def choisir_tirer(self):

        self.Player1.ajouter_carte(self.deck.pop())  # Ajoute une carte à la main du joueur
        self.carte_joueur(len(self.Player1.main), self.Player1.main[-1])  # Affiche la carte à la dernière position de la main
        self.updateScoreJoueur()    # Met à jour le score du joueur

        # vérification si le joueur a dépassé 21 (réutilisable aussi pour le dealer)
        if acteur_est_bust(self.Player1): # Utilise la fonction de fonctions.py
            self.tour_label.config(text="Vous avez dépassé 21 (Bust). Manche terminée.")
            self.scoreTotalDealer = scoreTotal(self.scoreTotalDealerLabel, self.Dealer, self.scoreTotalDealer)
            #Unpack les bouttons qui permettent de tirer et de rester
            self.bouton_tirer.config(state="disabled")
            self.bouton_rester.config(state="disabled")

    
        # Affichage pour les cartes du dealer
    def carte_dealer(self, numero_carte: int, carte: Cartes):
        affichageCarte(self.frameCartesDealer, carte, x=50*(numero_carte-1))


        # Affichage d'une carte face cachée pour le dealer
    def carte_dos_dealer(self, numero_carte: int): 
        # Création d'un Canvas pour la carte face cachée
        card = tk.Canvas(self.frameCartesDealer, width=200, height=300, bg="#c0c0c0", 
                         highlightthickness=2, highlightbackground="black") 
        card.place(x=50 * (numero_carte - 1), y=5) # Positionne la carte dans le frame du dealer
        card.create_rectangle(10, 10, 190, 290, outline="black") # Bordure de la carte
        card.create_text(100, 150, text="?", font=("Arial", 60), fill="black") # Symbole central
        return card


        # Affichage d'une carte dans le frame des cartes pour le joueur 
    def carte_joueur(self, numero_carte: int, carte: Cartes):
        affichageCarte(self.frameCartesJoueur, carte, x=50*(numero_carte-1))


    #Utilise la fonction updateScore pour updater avec des variables globales
    def updateScoreJoueur(self):
        updateScore(self.scoreMainJoueurLabel, self.Player1)


    
    # Logique lorsque le boutton "stay" est appuyé
    def choisir_rester(self):
        #bloque les bouttons qui permettent de tirer et rester
        self.bouton_tirer.config(state="disabled")
        self.bouton_rester.config(state="disabled")


        # si le croupier n’a pas encore de cartes visibles, on lui en met 2
        if len(self.Dealer.main) == 0: # Vérifie si le croupier a des cartes
            self.Dealer.ajouter_carte(self.deck.pop()); self.carte_dealer(1, self.Dealer.main[0]) # Affiche la première carte du croupier
            self.Dealer.ajouter_carte(self.deck.pop()); self.carte_dealer(2, self.Dealer.main[1]) # Affiche la deuxième carte du croupier

        # mémorise combien il avait de cartes avant de piocher
        mémoire_nb_cartes = len(self.Dealer.main)

        # Révéler la 2e carte cachée du dealer
        for carte in self.frameCartesDealer.winfo_children(): # Parcourt les cartes du dealer
            carte.destroy()  # efface les cartes actuelles
            self.carte_dealer(1, self.Dealer.main[0]) # Affiche la première carte du croupier
            self.carte_dealer(2, self.Dealer.main[1]) # Affiche la deuxième carte du croupier

        # Révéler la 2e carte si elle est cachée
        if self.dealer_carte_cachee is not None: 
            self.dealer_carte_cachee.destroy() # Supprime le dos de la carte
            self.dealer_carte_cachee = None # Réinitialise la variable
            self.carte_dealer(2, self.Dealer.main[1])  # on dessine la vraie 2e carte

        # le croupier joue tout seul (jusqu'à 17)
        tour_croupier(self.Dealer, self.deck)

        # dessine uniquement les nouvelles cartes tirées
        for i in range(mémoire_nb_cartes, len(self.Dealer.main)): 
            self.carte_dealer(i + 1, self.Dealer.main[i]) # Affiche les nouvelles cartes du croupier

        # verdict de la manche
        score_joueur = self.Player1.getScore() # Récupère le score du joueur
        score_dealer = self.Dealer.getScore() # Récupère le score du croupier
        if acteur_est_bust(self.Dealer): # fonction de fonctions.py
            verdict = "Vous avez gagné !"  # dealer bust
            self.scoreTotalJoueur = scoreTotal(self.scoreTotalJoueurLabel, self.Player1, self.scoreTotalJoueur)
        elif score_joueur > score_dealer:
            verdict = "Vous avez gagné !"
            self.scoreTotalJoueur = scoreTotal(self.scoreTotalJoueurLabel, self.Player1, self.scoreTotalJoueur)

        elif score_joueur < score_dealer:
            verdict = "Vous avez perdu"
            self.scoreTotalDealer = scoreTotal(self.scoreTotalDealerLabel, self.Dealer, self.scoreTotalDealer)
        else:
            verdict = "Égalité (push)"
        self.tour_label.config(text=f"Résultat — Joueur: {score_joueur} | Croupier: {score_dealer} → {verdict}")


    # Fonction pour démarrer une nouvelle partie
    def nouvelle_partie(self):
        #Débloque les boutons
        self.bouton_rester.config(state="normal")
        self.bouton_tirer.config(state="normal")

        # Réinitialiser self.deck et acteurs
        self.deck = creer_deck()
        self.Player1 = Joueur("Joueur 1")
        self.Dealer = Croupier()

        # Effacer les anciennes cartes affichées
        for carte in self.frameCartesJoueur.winfo_children(): # winfo_children() retourne une liste de tous les widgets (items) enfants du joueur
            carte.destroy() # efface les cartes actuelles
        for carte in self.frameCartesDealer.winfo_children(): # winfo_children() retourne une liste de tous les widgets (items) enfants du dealer
            carte.destroy() # efface les cartes actuelles

        # Réinitialiser le score affiché
        self.updateScoreJoueur() # Met à jour le score du joueur
        self.tour_label.config(text="Nouvelle partie — À votre tour : Tirer ou rester") # Réinitialise le label du tour

        # Nettoyer l'affichage dealer
        for c in self.frameCartesDealer.winfo_children():
            c.destroy()

        # self.Dealer : 1 carte visible + 1 dos
        self.Dealer.ajouter_carte(self.deck.pop())
        self.carte_dealer(1, self.Dealer.main[0])
        self.Dealer.ajouter_carte(self.deck.pop())
        dealer_cache_canvas = self.carte_dos_dealer(2)  # on mémorise le dos pour le révéler plus tard

        # Distribuer 2 cartes au joueur
        self.Player1.ajouter_carte(self.deck.pop())
        self.carte_joueur(1, self.Player1.main[0])
        self.Player1.ajouter_carte(self.deck.pop())
        self.carte_joueur(2, self.Player1.main[1])
        self.updateScoreJoueur()

        # Vérifie si le joueur a blackjack et le fait rester automatiquement si c'est le cas
        if self.Player1.getScore() == 21:
            self.choisir_rester()
