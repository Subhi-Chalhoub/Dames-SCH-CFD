import pygame

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
VERT = (0, 255, 0, 100)  # Vert transparent pour surbrillance
DIMENSION_CASE = 80

# Fonction pour dessiner le plateau
def dessiner_plateau(fenetre, NOMBRE_CASES):
    for ligne in range(NOMBRE_CASES):
        for colonne in range(NOMBRE_CASES):
            x = ligne * DIMENSION_CASE
            y = colonne * DIMENSION_CASE
            rectangle_case = pygame.Rect(x, y, DIMENSION_CASE, DIMENSION_CASE)
            if (ligne + colonne) % 2 == 0:
                pygame.draw.rect(fenetre, NOIR, rectangle_case)
            else:
                pygame.draw.rect(fenetre, BLANC, rectangle_case)

# Fonction pour dessiner les pions
def dessiner_pions(fenetre, pions_blancs, pions_noirs, pion_image_blanc, pion_image_noir):
    for pion in pions_blancs:
        fenetre.blit(pion_image_blanc, (pion[0] * DIMENSION_CASE, pion[1] * DIMENSION_CASE))
    for pion in pions_noirs:
        fenetre.blit(pion_image_noir, (pion[0] * DIMENSION_CASE, pion[1] * DIMENSION_CASE))

# Fonction pour afficher la surbrillance d'une case
def afficher_surbrillance(fenetre, position_selectionnee, DIMENSION_CASE, VERT):
    if position_selectionnee:
        surbrillance = pygame.Surface((DIMENSION_CASE, DIMENSION_CASE), pygame.SRCALPHA)
        surbrillance.fill(VERT)
        fenetre.blit(surbrillance, (position_selectionnee[0] * DIMENSION_CASE, position_selectionnee[1] * DIMENSION_CASE))

# Fonction pour afficher le texte du tour actuel
def afficher_texte_tour(fenetre, FONT, tour_blanc):
    texte_tour = FONT.render(f"Tour : {'Bleu' if tour_blanc else 'Rouge'}", True, NOIR)
    fenetre.blit(texte_tour, (10, 10))
