
# Fonction pour trouver le pion à une position
def trouver_pion(position, pions):
    for pion in pions:
        if pion == position:
            return pion
    return None

# Fonction pour vérifier si un mouvement est valide
def mouvement_valide(pion, nouvelle_position, pions_allies, pions_ennemis, tour_blanc):
    dx = nouvelle_position[0] - pion[0]
    dy = nouvelle_position[1] - pion[1]

    # Mouvement en diagonale simple
    if abs(dx) == 1 and dy == (1 if tour_blanc else -1):
        return True

    # Capture d'un pion adverse
    elif abs(dx) == 2 and dy == (2 if tour_blanc else -2):
        pion_intermediaire = [pion[0] + dx // 2, pion[1] + dy // 2]
        if pion_intermediaire in pions_ennemis:
            pions_ennemis.remove(pion_intermediaire)  # Retirer le pion capturé
            return True

    return False

# Fonction pour promouvoir un pion en reine
def promouvoir_si_necessaire(pion, tour_blanc, NOMBRE_CASES):
    if (tour_blanc and pion[1] == NOMBRE_CASES - 1) or (not tour_blanc and pion[1] == 0):
        return True  # Indique qu'il devient une reine
    return False
