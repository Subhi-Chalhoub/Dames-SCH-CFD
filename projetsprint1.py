import pygame

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("sprint1")

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
TAILLE_CASE, NOMBRE_CASES = 80, 10
position_pion = 0



# Charger l'image du pion
pion_image = pygame.image.load("MA-24_pion.png")
pion_image = pygame.transform.scale(pion_image,
                                    (TAILLE_CASE, TAILLE_CASE))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Assure la sortie complète du programme
        if event.type == pygame.KEYDOWN:
            # Déplacement vers la droite
            if event.key == pygame.K_RIGHT:
                position_pion = min(position_pion + 1, NOMBRE_CASES - 1)  # Limite le pion au bord droit
            # Déplacement vers la gauche
            elif event.key == pygame.K_LEFT:
                position_pion = max(position_pion - 1, 0) # Limite le pion au bord gauche
            elif event.key == pygame.K_DOWN:
                position_pion[1] = min(position_pion[1] +1, NOMBRE_CASES -1 )
            elif event.key == pygame.K_UP:
                position_pion[1] = max(position_pion[1] -1, 0)

    # Dessin de la ligne et du pion
    fenetre.fill(BLANC)

    for ligne in range (10):
        for colonne in range (10):
            x = ligne * TAILLE_CASE
            y = colonne * TAILLE_CASE
            rectangle_case = pygame.Rect(x, y, TAILLE_CASE, TAILLE_CASE)
            if (ligne + colonne) % 2 == 0:
                pygame.draw.rect(fenetre, (0,0,0), rectangle_case)
            else:
                pygame.draw.rect(fenetre, (0, 0, 0), rectangle_case, 1)


    # Affiche l'image du pion à la position actuelle
    fenetre.blit(pion_image, (position_pion * TAILLE_CASE, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limite la vitesse de la boucle

    #commm