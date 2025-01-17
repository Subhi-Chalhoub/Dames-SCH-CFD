import pygame

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)  # Définition des couleurs pour le fond des cases
VERT = (0, 255, 0, 100)  # Vert transparent pour la surbrillance d'une case
DIMENSION_CASE = 80  # Taille des cases sur le plateau


# Fonction pour dessiner le plateau de jeu
def dessiner_plateau(fenetre, NOMBRE_CASES):
    for ligne in range(NOMBRE_CASES):
        for colonne in range(NOMBRE_CASES):
            x = ligne * DIMENSION_CASE  # Position x de la case
            y = colonne * DIMENSION_CASE  # Position y de la case
            rectangle_case = pygame.Rect(x, y, DIMENSION_CASE,
                                         DIMENSION_CASE)  # Définir la taille et la position de la case
            if (ligne + colonne) % 2 == 0:  # Alterner entre cases noires et blanches
                pygame.draw.rect(fenetre, NOIR, rectangle_case)  # Dessiner une case noire
            else:
                pygame.draw.rect(fenetre, BLANC, rectangle_case)  # Dessiner une case blanche


# Fonction pour dessiner les pions et reines sur le plateau
def dessiner_pions(fenetre, pions_blancs, pions_noirs, pion_image_blanc, pion_image_noir, reine_image_blanc,
                   reine_image_noir):
    # Dessiner les pions blancs
    for pion in pions_blancs:
        # Vérifier si le pion est une reine (dictionnaire avec la clé 'reine')
        image = reine_image_blanc if isinstance(pion, dict) and pion.get("reine") else pion_image_blanc
        # Calculer la position de chaque pion et dessiner l'image sur la fenêtre
        fenetre.blit(image, ((pion["position"][0] * DIMENSION_CASE, pion["position"][1] * DIMENSION_CASE)
                             if isinstance(pion, dict) else (pion[0] * DIMENSION_CASE, pion[1] * DIMENSION_CASE)))

    # Dessiner les pions noirs
    for pion in pions_noirs:
        # Vérifier si le pion est une reine (dictionnaire avec la clé 'reine')
        image = reine_image_noir if isinstance(pion, dict) and pion.get("reine") else pion_image_noir
        # Calculer la position de chaque pion et dessiner l'image sur la fenêtre
        fenetre.blit(image, ((pion["position"][0] * DIMENSION_CASE, pion["position"][1] * DIMENSION_CASE)
                             if isinstance(pion, dict) else (pion[0] * DIMENSION_CASE, pion[1] * DIMENSION_CASE)))


# Fonction pour afficher la surbrillance d'une case (pour indiquer une sélection)
def afficher_surbrillance(fenetre, position_selectionnee, DIMENSION_CASE, VERT):
    if position_selectionnee:  # Si une case est sélectionnée
        surbrillance = pygame.Surface((DIMENSION_CASE, DIMENSION_CASE),
                                      pygame.SRCALPHA)  # Créer une surface pour la surbrillance
        surbrillance.fill(VERT)  # Remplir la surface de la couleur verte
        # Dessiner la surbrillance sur la fenêtre à la position de la case sélectionnée
        fenetre.blit(surbrillance,
                     (position_selectionnee[0] * DIMENSION_CASE, position_selectionnee[1] * DIMENSION_CASE))


# Fonction pour afficher le texte du tour actuel (indique quel joueur doit jouer)
 #fait par chatgpt
def afficher_texte_tour(fenetre, FONT, tour_blanc):
    # Rendre le texte indiquant le tour actuel (Bleu pour les blancs, Rouge pour les noirs)
    texte_tour = FONT.render(f"Tour : {'Bleu' if tour_blanc else 'Rouge'}", True, NOIR)
    # Afficher le texte en haut à gauche de la fenêtre
    fenetre.blit(texte_tour, (10, 10))