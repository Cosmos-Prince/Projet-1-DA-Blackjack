# Calculer le score

def calculer_score(main):
    score = sum(card.getValeur() for card in main)
    if score > 21 and any(card.getChiffre() == 'A' for card in main):
        score -= 10
    return score

