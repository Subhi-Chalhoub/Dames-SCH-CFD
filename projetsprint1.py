import pygame

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("sprint1")

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
TAILLE_CASE, NOMBRE_CASES = (75, 10)
position_pion_blanc = [0, 0]
position_pion_noir = [1,9]

nb_pion = 20
nb_pion_noir = 20

# Charger l'image du pion
pion_image = pygame.image.load("pion3DCV2.png")
pion_image = pygame.transform.scale(pion_image,
                                    (TAILLE_CASE, TAILLE_CASE))

pion_image_noir = pygame.image.load("pion3DV2.png")
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
                position_pion_blanc[0] = min(position_pion_blanc[0] + 1, NOMBRE_CASES - 1)  # Limite le pion au bord droit
                position_pion_blanc[1] = min(position_pion_blanc[1] + 1, NOMBRE_CASES - 1)  # Limite le pion au bord bas
            # Déplacement vers la gauche
            elif event.key == pygame.K_LEFT:
                position_pion_blanc[0] = max(position_pion_blanc[0] - 1, 0)
                position_pion_blanc[1] = min(position_pion_blanc[1] + 1, NOMBRE_CASES - 1)




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
    pions_places_blanc = 0
    for ligne in range(4):
        for colonne in range(10):
            if (ligne + colonne) % 2 == 0:
                if pions_places_blanc < nb_pion:
                    y = colonne * TAILLE_CASE
                    x = ligne * TAILLE_CASE
                    fenetre.blit(pion_image, (y, x))
                    pions_places_blanc += 1


    pions_places = 0
    for ligne in range(4):
        for colonne in range(10):
            if (ligne + colonne) % 2 == 0:
                if pions_places < nb_pion_noir:
                    y = colonne * TAILLE_CASE
                    x = ligne * TAILLE_CASE+6*TAILLE_CASE
                    fenetre.blit(pion_image_noir, (y, x))
                    pions_places -= 1


    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limite la vitesse de la boucle
