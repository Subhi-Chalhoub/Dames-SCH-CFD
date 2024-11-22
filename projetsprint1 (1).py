import pygame

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((1000, 100))
pygame.display.set_caption("sprint1")

# Couleurs et paramètres
BLANC, NOIR = (255, 255, 255), (0, 0, 0)
TAILLE_CASE, NOMBRE_CASES = 100, 10
position_pion = 0

# Charger l'image du pion
pion_image = pygame.image.load("MA-24_pion.png")
pion_image = pygame.transform.scale(pion_image,
                                    (TAILLE_CASE, TAILLE_CASE))
# test
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
                position_pion = max(position_pion - 1, 0)  # Limite le pion au bord gauche

    # Dessin de la ligne et du pion
    fenetre.fill(BLANC)

    for i in range(NOMBRE_CASES):
        couleur = NOIR if i % 2 == 0 else BLANC
        pygame.draw.rect(fenetre, couleur, (i * TAILLE_CASE, 0, TAILLE_CASE, 100))

    # Affiche l'image du pion à la position actuelle
    fenetre.blit(pion_image, (position_pion * TAILLE_CASE, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limite la vitesse de la boucle