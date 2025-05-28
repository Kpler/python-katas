from poker.with_read_input.poker import HandRank

def compute_winner(hands: list[HandRank]) -> int:
    # Associer chaque main à son index original
    indexed_hands = list(enumerate(hands))

    # Tri par type (valeur numérique la plus élevée d'abord) puis par valeurs
    sorted_hands = sorted(indexed_hands, key=lambda x: (x[1].type.value, x[1].values), reverse=True)

    # Retourner l'index original de la main gagnante
    return sorted_hands[0][0]
