
# Fonction pour trouver le pion à une position
def trouver_pion(position, pions):
    for pion in pions:
        if isinstance(pion, dict):
            if pion["position"] == position:
                return pion
        elif pion == position:
            return pion
    return None

# Fonction pour vérifier si un mouvement est valide
# La def a été faite par chatgpt jusqu'à "returne false "
def mouvement_valide(pion, nouvelle_position, pions_allies, pions_ennemis, tour_blanc):
    # Récupérer la position du pion, qu'il soit un dictionnaire (reine) ou une liste (pion normal)
    position_pion = pion["position"] if isinstance(pion, dict) else pion
    dx = nouvelle_position[0] - position_pion[0]
    dy = nouvelle_position[1] - position_pion[1]

    # Déplacement pour les reines

    if isinstance(pion, dict) and pion.get("reine"):
        if abs(dx) == abs(dy):  # Déplacement diagonal
            step_x = dx // abs(dx)
            step_y = dy // abs(dy)
            x, y = position_pion
            for _ in range(abs(dx) - 1):  # Vérifier si le chemin est libre
                x += step_x
                y += step_y
                if [x, y] in pions_allies + pions_ennemis:
                    return False
            return True

    # Mouvement en diagonale simple pour un pion normal
    if abs(dx) == 1 and dy == (1 if tour_blanc else -1):
        return True

    # Capture d'un pion adverse
    elif abs(dx) == 2 and dy == (2 if tour_blanc else -2):
        pion_intermediaire = [position_pion[0] + dx // 2, position_pion[1] + dy // 2]
        if pion_intermediaire in pions_ennemis:
            pions_ennemis.remove(pion_intermediaire)  # Retirer le pion capturé
            return True

    return False


# Fonction pour promouvoir un pion en reine
def promouvoir_si_necessaire(pion, tour_blanc, NOMBRE_CASES):
    if (tour_blanc and pion[1] == NOMBRE_CASES - 1) or (not tour_blanc and pion[1] == 0):
        return True  # Indique qu'il devient une reine
    return False
