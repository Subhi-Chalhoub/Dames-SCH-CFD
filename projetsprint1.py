import pygame

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("sprint1")

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
TAILLE_CASE, NOMBRE_CASES = 80, 10
position_pion = [0, 0]
position_pion_noir = [9,9]

# Charger l'image du pion
pion_image = pygame.image.load("MA-24_pion.png")
pion_image = pygame.transform.scale(pion_image,
                                    (TAILLE_CASE, TAILLE_CASE))

pion_image_noir = pygame.image.load("MA-24_pion_noir.png")
pion_image_noir = pygame.transform.scale(pion_image_noir,
                                    (TAILLE_CASE, TAILLE_CASE))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # Déplacement vers la droite
            if event.key == pygame.K_RIGHT:
                position_pion[0] = min(position_pion[0] + 1, NOMBRE_CASES - 1)  # Limite le pion au bord droit
                position_pion[1] = min(position_pion[1] + 1, NOMBRE_CASES - 1)  # Limite le pion au bord bas
            # Déplacement vers la gauche
            elif event.key == pygame.K_LEFT:
                position_pion[0] = max(position_pion[0] - 1, 0)
                position_pion[1] = min(position_pion[1] + 1, NOMBRE_CASES - 1)


    fenetre.fill(BLANC)

    for ligne in range(10):
        for colonne in range(10):
            x = ligne * TAILLE_CASE
            y = colonne * TAILLE_CASE
            rectangle_case = pygame.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
            if (ligne + colonne) % 2 == 0:
                pygame.draw.rect(fenetre, (0, 0, 0), rectangle_case)
            else:
                pygame.draw.rect(fenetre, (255, 255, 255), rectangle_case, 1)

    # Affiche l'image du pion à la position actuelle
    fenetre.blit(pion_image, (position_pion[0] * TAILLE_CASE, position_pion[1] * TAILLE_CASE))
    fenetre.blit(pion_image_noir, (position_pion_noir[0] * TAILLE_CASE, position_pion_noir[1] * TAILLE_CASE))

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limite la vitesse de la boucle
