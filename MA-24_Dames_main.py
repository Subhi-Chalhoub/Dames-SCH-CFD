import pygame
from ma24_dames_gfx import dessiner_plateau, dessiner_pions, afficher_surbrillance, afficher_texte_tour
from ma24_dames_rules import trouver_pion, mouvement_valide, promouvoir_si_necessaire

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jeu de Dames")
BLANC = (255, 255, 255)
VERT = (0, 255, 0, 100)

# Charger l'image des pions et des reines
try:
    pion_image_blanc = pygame.image.load("pion2_1_bleu.png")
    pion_image_blanc = pygame.transform.scale(pion_image_blanc, (80, 80))

    pion_image_noir = pygame.image.load("pion2_3_rouge.png")
    pion_image_noir = pygame.transform.scale(pion_image_noir, (80, 80))

    reine_image_blanc = pygame.image.load("reine_bleue.png")
    reine_image_blanc = pygame.transform.scale(reine_image_blanc, (80, 80))

    reine_image_noir = pygame.image.load("reine_rouge.png")
    reine_image_noir = pygame.transform.scale(reine_image_noir, (80, 80))
except pygame.error as e:
    print("Erreur lors du chargement des images :", e)
    pygame.quit()
    exit()

# Variables du jeu
NOMBRE_CASES = 10
DIMENSION_CASE = 80
FONT = pygame.font.Font(None, 36)

# Position des pions
pions_blancs = [[col, row] for row in range(4) for col in range(NOMBRE_CASES) if (row + col) % 2 == 0]
pions_noirs = [[col, row + 6] for row in range(4) for col in range(NOMBRE_CASES) if (row + col) % 2 == 0]

# Variables pour le jeu
position_selectionnee = None
tour_blanc = True  # Blanc commence

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
                    if mouvement_valide(position_selectionnee, [case_x, case_y], pions_actuels, pions_ennemis, tour_blanc):
                        position_selectionnee[0] = case_x
                        position_selectionnee[1] = case_y

                        # Vérifiez si le pion doit être promu
                        if promouvoir_si_necessaire(position_selectionnee, tour_blanc, NOMBRE_CASES):
                            pions_actuels.remove(position_selectionnee)
                            pions_actuels.append({"position": [case_x, case_y], "reine": True})

                        tour_blanc = not tour_blanc  # Changer de tour
                position_selectionnee = None
            else:
                # Vérifier si un pion est sélectionné
                pions_actuels = pions_blancs if tour_blanc else pions_noirs
                position_selectionnee = trouver_pion([case_x, case_y], pions_actuels)

    # Dessiner l'échiquier et les pions
    fenetre.fill(BLANC)
    dessiner_plateau(fenetre, NOMBRE_CASES)
    dessiner_pions(fenetre, pions_blancs, pions_noirs, pion_image_blanc, pion_image_noir, reine_image_blanc, reine_image_noir)

    # Afficher la surbrillance et le texte du tour
    afficher_surbrillance(fenetre, position_selectionnee, DIMENSION_CASE, VERT)
    afficher_texte_tour(fenetre, FONT, tour_blanc)

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limiter la vitesse de la boucle
