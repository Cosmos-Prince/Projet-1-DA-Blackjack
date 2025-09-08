# Calculer le score pour le Blackjack
def calculer_score(main):
    score = sum(card.value for card in main)
    if score > 21 and any(card.rank == 'A' for card in main):
        score -= 10
    return score