# Fonction pour trouver le pion à une position donnée
def trouver_pion(position, pions):
    for pion in pions:
        if isinstance(pion, dict):  # Si c'est une reine (dictionnaire)
            if pion["position"] == position:  # Vérifier si la position correspond
                return pion
        elif pion == position:  # Si c'est un pion normal (liste)
            return pion
    return None  # Si aucun pion n'est trouvé à cette position


# Fonction pour vérifier si un mouvement est valide
# la def du mouvement a été faite par monsieur chatgpt
def mouvement_valide(pion, nouvelle_position, pions_allies, pions_ennemis, tour_blanc):
    # Récupérer la position du pion, qu'il soit une reine (dictionnaire) ou un pion normal (liste)
    position_pion = pion["position"] if isinstance(pion, dict) else pion
    dx = nouvelle_position[0] - position_pion[0]  # Calcul de la différence en x
    dy = nouvelle_position[1] - position_pion[1]  # Calcul de la différence en y

    # Déplacement pour les reines
    if isinstance(pion, dict) and pion.get("reine"):  # Si c'est une reine
        if abs(dx) == abs(dy):  # Le déplacement doit être diagonale
            step_x = dx // abs(dx)  # Calcul de l'étape en x
            step_y = dy // abs(dy)  # Calcul de l'étape en y
            x, y = position_pion
            for _ in range(abs(dx) - 1):  # Vérifier si le chemin est libre entre les cases
                x += step_x
                y += step_y
                if [x, y] in pions_allies + pions_ennemis:  # Si une case est occupée
                    return False  # Mouvement est invalide
            return True  # Mouvement valide pour une reine

        # Capture d'un pion adverse (mouvement de deux cases) dans les deux sens pour une reine
        elif abs(dx) == 2 and abs(dy) == 2:  # Capture possible (mouvement de deux cases)
            # Calculer la position du pion capturé
            pion_intermediaire = [position_pion[0] + dx // 2, position_pion[1] + dy // 2]
            if pion_intermediaire in pions_ennemis:  # Si le pion adverse est à la position intermédiaire
                pions_ennemis.remove(pion_intermediaire)  # Retirer le pion capturé
                return True  # Capture valide
            else:
                return False  # Pas de pion ennemi à capturer

    # Mouvement en diagonale simple pour un pion normal
    if abs(dx) == 1 and (dy == (1 if tour_blanc else -1) or dy == (-1 if tour_blanc else 1)):  # Déplacement d'un pion normal
        return True  # Mouvement valide

    # Capture d'un pion adverse (mouvement de deux cases) pour un pion normal
    elif abs(dx) == 2 and (dy == (2 if tour_blanc else -2) or dy == (-2 if tour_blanc else 2)):  # Capture d'un pion adverse
        pion_intermediaire = [position_pion[0] + dx // 2, position_pion[1] + dy // 2]  # Calculer la position du pion capturé
        if pion_intermediaire in pions_ennemis:  # Si le pion adverse est à la position intermédiaire
            pions_ennemis.remove(pion_intermediaire)  # Retirer le pion capturé
            return True  # Capture valide

    return False  # Si aucune condition n'est remplie, le mouvement est invalide




# Fonction pour promouvoir un pion en reine lorsqu'il atteint la dernière ligne
def promouvoir_si_necessaire(pion, tour_blanc, NOMBRE_CASES):
    if (tour_blanc and pion[1] == NOMBRE_CASES - 1) or (not tour_blanc and pion[1] == 0):  # Si le pion atteint la dernière ligne
        return True  # Le pion devient une reine
    return False  # Le pion reste un pion normal