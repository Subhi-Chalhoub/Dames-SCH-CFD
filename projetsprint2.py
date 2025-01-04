import pygame

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jeu de Dames")

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
VERT = (0, 255, 0, 100)  # Vert transparent pour surbrillance
DIMENSION_CASE, NOMBRE_CASES = 80, 10
FONT = pygame.font.Font(None, 36)

# Charger l'image des pions
try:
    pion_image_blanc = pygame.image.load("MA-24_pion.png")
    pion_image_blanc = pygame.transform.scale(pion_image_blanc, (DIMENSION_CASE, DIMENSION_CASE))

    pion_image_noir = pygame.image.load("MA-24_pion_noir.png")
    pion_image_noir = pygame.transform.scale(pion_image_noir, (DIMENSION_CASE, DIMENSION_CASE))
except pygame.error as e:
    print("Erreur lors du chargement des images :", e)
    pygame.quit()
    exit()

# Position des pions blancs et noirs
pions_blancs = [[col, row] for row in range(4) for col in range(NOMBRE_CASES) if (row + col) % 2 == 0]
pions_noirs = [[col, row + 6] for row in range(4) for col in range(NOMBRE_CASES) if (row + col) % 2 == 0]

# Variables pour le jeu
position_selectionnee = None
tour_blanc = True  # Blanc commence


# Fonction pour dessiner le plateau
def dessiner_plateau():
    for ligne in range(NOMBRE_CASES):
        for colonne in range(NOMBRE_CASES):
            x = ligne * DIMENSION_CASE
            y = colonne * DIMENSION_CASE
            rectangle_case = pygame.Rect(x, y, DIMENSION_CASE, DIMENSION_CASE)
            if (ligne + colonne) % 2 == 0:
                pygame.draw.rect(fenetre, NOIR, rectangle_case)
            else:
                pygame.draw.rect(fenetre, BLANC, rectangle_case)


# Fonction pour trouver le pion à une position
def trouver_pion(position, pions):
    for pion in pions:
        if pion == position:
            return pion
    return None


# Fonction pour vérifier si un mouvement est valide
def mouvement_valide(pion, nouvelle_position, pions_allies, pions_ennemis):
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


# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Récupérer la position du clic
            x, y = event.pos
            case_x, case_y = x // DIMENSION_CASE, y // DIMENSION_CASE

            if position_selectionnee:
                # Si un pion est sélectionné, vérifier le mouvement
                if [case_x, case_y] not in pions_blancs + pions_noirs:  # Case libre
                    pions_actuels = pions_blancs if tour_blanc else pions_noirs
                    pions_ennemis = pions_noirs if tour_blanc else pions_blancs
                    if mouvement_valide(position_selectionnee, [case_x, case_y], pions_actuels, pions_ennemis):
                        position_selectionnee[0] = case_x
                        position_selectionnee[1] = case_y
                        tour_blanc = not tour_blanc  # Changer de tour
                position_selectionnee = None
            else:
                # Vérifier si un pion est sélectionné
                pions_actuels = pions_blancs if tour_blanc else pions_noirs
                position_selectionnee = trouver_pion([case_x, case_y], pions_actuels)

    # Dessiner l'échiquier
    fenetre.fill(BLANC)
    dessiner_plateau()

    # Dessiner les pions blancs
    for pion in pions_blancs:
        fenetre.blit(pion_image_blanc, (pion[0] * DIMENSION_CASE, pion[1] * DIMENSION_CASE))

    # Dessiner les pions noirs
    for pion in pions_noirs:
        fenetre.blit(pion_image_noir, (pion[0] * DIMENSION_CASE, pion[1] * DIMENSION_CASE))

    # Mettre en surbrillance la case sélectionnée
    if position_selectionnee:
        surbrillance = pygame.Surface((DIMENSION_CASE, DIMENSION_CASE), pygame.SRCALPHA)
        surbrillance.fill(VERT)
        fenetre.blit(surbrillance, (position_selectionnee[0] * DIMENSION_CASE, position_selectionnee[1] * DIMENSION_CASE))

    # Afficher le tour actuel
    texte_tour = FONT.render(f"Tour : {'Blancs' if tour_blanc else 'Noirs'}", True, NOIR)
    fenetre.blit(texte_tour, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limiter la vitesse de la boucle