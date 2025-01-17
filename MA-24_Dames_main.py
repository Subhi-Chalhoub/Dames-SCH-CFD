import pygame

from ma24_dames_gfx import dessiner_plateau, dessiner_pions, afficher_surbrillance, afficher_texte_tour
# Importation des fonctions liées à l'affichage graphique du jeu
from ma24_dames_rules import trouver_pion, mouvement_valide, promouvoir_si_necessaire
# Importation des règles et fonctions de gestion du jeu

# Initialiser Pygame et la fenêtre
pygame.init()
fenetre = pygame.display.set_mode((800, 800)) # Initialisation de la fenêtre du jeu avec une taille de 800x800
pygame.display.set_caption("Jeu de Dames") # Titre de la fenêtre
BLANC = (255, 255, 255) # Couleur blanche pour le plateau
VERT = (0, 255, 0, 100)  # Vert transparent utilisé pour la surbrillance
ROUGE = (255, 0, 0) # Rouge pour l'équipe adverse
BLEU = (0, 0, 255) # Bleu pour l'équipe alliée

# Charger l'image des pions et des reines
try:
    # image pion simple bleu.png
    pion_image_blanc = pygame.image.load("pion2_1_bleu.png")
    pion_image_blanc = pygame.transform.scale(pion_image_blanc, (80, 80))

    # image pion simple rouge.png
    pion_image_noir = pygame.image.load("pion2_3_rouge.png")
    pion_image_noir = pygame.transform.scale(pion_image_noir, (80, 80))

    # image pion reine bleue.png
    reine_image_blanc = pygame.image.load("reine_bleue.png")
    reine_image_blanc = pygame.transform.scale(reine_image_blanc, (80, 80))

    # image pion reine rouge.png
    reine_image_noir = pygame.image.load("reine_rouge.png")
    reine_image_noir = pygame.transform.scale(reine_image_noir, (80, 80))

except pygame.error as e: # Ce bloc s'exécute si une erreur spécifique à Pygame
    print("Erreur lors du chargement des images :", e) # Affiche un message d'erreur détaillant le problème rencontré
    pygame.quit() # Ferme proprement tous les modules  par Pygame libére les ressources utilisées
    exit() # Termine immédiatement l'exécution du programme

# Variables du jeu
NOMBRE_CASES = 10 # Nombre de cases par ligne et par colonne
DIMENSION_CASE = 80 # Taille de chaque case avec pixel
FONT = pygame.font.Font(None, 36) # Police pour le texte normal
GRAND_FONT = pygame.font.Font(None, 100) # Police pour le texte d'annonce du gagnant

# Position des pions
pions_blancs = [[col, row] for row in range(4) for col in range(NOMBRE_CASES) if (row + col) % 2 == 0]
# Les pions blancs occupent les 4 premières rangées sur les cases noires
pions_noirs = [[col, row + 6] for row in range(4) for col in range(NOMBRE_CASES) if (row + col) % 2 == 0]
# Les pions noirs occupent les 4 dernières rangées sur les cases noires

# Variables pour le jeu
position_selectionnee = None # Stocke la position du pion actuellement sélectionné
tour_blanc = True  # Blanc commence
jeu_termine = False  # Booléen pour vérifier si le jeu est terminé

# fait par chatgpt
# Fonction pour afficher le gagnant
def afficher_gagnant(fenetre, gagnant):
    # Création du texte à afficher, avec une couleur en fonction de l'équipe gagnante
    texte_gagnant = GRAND_FONT.render(f"L'équipe {gagnant} a gagné!", True, BLEU if gagnant == "Bleu" else ROUGE)#True, BLEU if gagnant == "Bleu" else ROUGE représente la couleur du texte : bleu pour l'équipe Bleue, rouge pour l'équipe Rouge
    # Le message à afficher, incluant le nom de l'équipe gagnante (Bleu ou Rouge)
    fenetre.blit(texte_gagnant, (400 - texte_gagnant.get_width() // 2, 400 - texte_gagnant.get_height() // 2))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
            pygame.quit()
            exit()

        if not jeu_termine and event.type == pygame.MOUSEBUTTONDOWN:
            # Récupérer la position du clic
            x, y = event.pos # Coordonnées du clic
            case_x, case_y = x // DIMENSION_CASE, y // DIMENSION_CASE

            if position_selectionnee:
                # Si un pion est sélectionné, vérifier le mouvement
                if [case_x, case_y] not in [p["position"] if isinstance(p, dict) else p for p in pions_blancs + pions_noirs]:  # Case libre
                    pions_actuels = pions_blancs if tour_blanc else pions_noirs # Pions de l'équipe active
                    pions_ennemis = pions_noirs if tour_blanc else pions_blancs # Pions de l'équipe adverse
                    if mouvement_valide(position_selectionnee, [case_x, case_y], pions_actuels, pions_ennemis, tour_blanc):
                        # Mise à jour de la position si mouvement est valide
                        if isinstance(position_selectionnee, dict):  # Si c'est une reine représenter par le dictionnaire
                            position_selectionnee["position"] = [case_x, case_y] # Met à jour la position de la reine avec les nouvelles coordonnées
                        else:
                            position_selectionnee[0] = case_x # Met à jour la coordonnée x du pion
                            position_selectionnee[1] = case_y # Met à jour la coordonnée y du pion

                        # Vérifiez si le pion doit être promu en reine
                        #ceci qui est fait par chatgpt
                        if not isinstance(position_selectionnee, dict) and promouvoir_si_necessaire(position_selectionnee, tour_blanc, NOMBRE_CASES):
                            pions_actuels.remove(position_selectionnee)
                            pions_actuels.append({"position": [case_x, case_y], "reine": True})

                        tour_blanc = not tour_blanc  # Changer de tour
                position_selectionnee = None # Réinitialise la sélection
            else:
                # Vérifier si un pion est sélectionné
                pions_actuels = pions_blancs if tour_blanc else pions_noirs
                position_selectionnee = trouver_pion([case_x, case_y], pions_actuels)

    # Vérifier les conditions de fin de jeu (victoire)
    # fait par chatgpt
    if not jeu_termine: # Vérifie si le jeu est encore en cours
        if not pions_blancs: # Si la liste des pions blancs est vide
            jeu_termine = True # Déclare que le jeu est terminé
            gagnant = "Rouge" # L'équipe rouge est déclarée gagnante
        elif not pions_noirs: # Sinon, si la liste des pions noirs est vide
            jeu_termine = True # Déclare que le jeu est terminé
            gagnant = "Bleu" # L'équipe bleue est déclarée gagnante

    # Dessiner l'échiquier et les pions (plateau, pions, surbrillance)
    fenetre.fill(BLANC) # Efface la fenêtre en blanc
    dessiner_plateau(fenetre, NOMBRE_CASES) # Dessine le plateau
    dessiner_pions(fenetre, pions_blancs, pions_noirs, pion_image_blanc, pion_image_noir, reine_image_blanc, reine_image_noir) # Dessine les pions

    # Afficher la surbrillance et le texte du tour actuel
    # fait par chatgpt
    if not jeu_termine:
        afficher_surbrillance(fenetre, position_selectionnee["position"] if isinstance(position_selectionnee, dict) else position_selectionnee, DIMENSION_CASE, VERT)
        # Vérifie si la position sélectionnée est un dictionnaire représente la reine
        # et utilise sa clé "position". Sinon, utilise directement la position sélectionnée
        afficher_texte_tour(fenetre, FONT, tour_blanc)  # Affiche de qui c'est le tour
    else:
        afficher_gagnant(fenetre, gagnant) # Affiche le gagnant une fois le jeu terminé

    pygame.display.flip() # Actualise l'affichage complet de la fenêtre pour les modifications apportées
    pygame.time.Clock().tick(30)  # Limiter la vitesse de la boucle