from doctest import testmod
from math import sqrt
from random import randint, random
from time import sleep

from upemtk import *

# Dimensions du jeu.
SQUARE_SIZE = 15
BOARD_WIDTH = 40  # 40
BOARD_HEIGHT = 30  # 30
BAR_HEIGHT = 35
COLORS = ["red", "orange", "gold", "yellow", "yellowgreen", "limegreen", "green", "teal", "darkcyan", "lightseagreen",
          "mediumturquoise", "deepskyblue", "dodgerblue", "royalblue", "blue", "indigo", "darkorchid", "mediumorchid",
          "orchid", "deeppink", "crimson"]
OUTLINE_COLORS = ["darkred", "darkorange", "goldenrod", "gold", "olivedrab", "forestgreen", "darkgreen",
                  "darkslategray", "darkslategrey", "darkcyan", "lightseagreen", "steelblue", "lightslategrey",
                  "slategrey", "darkblue", "black", "darkviolet", "blueviolet", "darkorchid", "mediumvioletred",
                  "firebrick"]
START_FRAMERATE = 10


# INFORMATIONS SUR LE PROGRAMME
#
# Le jeu est doté d'un menu pause, appuyez sur P pour faire pause.
# Le serpent se déplace avec les flèches directionelles.
#
# La pomme augmente la longueur du serpent de 1.
# Les cerises augmentent la longueur du serpent de 3.
# La bombe diminue la longueur du serpent de 2.
# Le score correspond à la taille du serpent (sans la tête).
#
# La vitesse augmente de 0.1 toutes les 10 secondes.
# Les obstacles sont limités en nombre, ce denier dépend directement du
# plateau de jeu. Les plus anciens vont donc être supprimés au fur et à mesure.
#
# Une bombe ne peut rester plus de dix secondes.
# Le chiffre inscrit sur une bombe indique les dégâts (points retirés en cas d'impact).
# Les dégâts causés par une bombe augmentent avec la vitesse.
#
# Le bonus étoile confère 10 secondes d'invincibilité, d'arène torique et de vitesse doublée.
# Le bonus torique inverse la toricité de l'arène pendant 15 secondes.
# Le bonus vitesse double la vitesse pendant 15 secondes.
# Le bonus mangeur de bombes transforme les bombes en bonus
# (ajouter des points au lieu d'en retirer) pendant 20 secondes.
#
# Si un serpent se mange lui-même, il perd.
# Si un serpent heurte un mur (dans une arène non-torique), il perd.
# Si un serpent heurte un obstacle, il perd.
#
# En multijoueur, le deuxième serpent se déplace avec les touches Z, Q, S et D.)
# En raison de difficultés techniques, il est impossible de faire égalité en multijoueur.


def get_time(framerate: int, rules: dict):
    """
    Calcule le temps en secondes écoulé depuis le début de la partie.
    :param int framerate: Taux de rafraichissement.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return int: Temps en secondes écoulé.
    """
    return rules["count"] // framerate


def get_score():
    """
    Calcule le score actuel en fonction de la longueur du serpent.
    :return int: Score actuel.
    """
    return len(snakes[0]) - 1


def format_time(time: int):
    """
    Formatte le temps sous la forme 'mm:ss' avec m pour les minutes et s pour les secondes.
    :param int time: Temps à formater.
    :return str: Temps formatté.

    >>> format_time(90)
    '01:30'
    """
    minutes = time // 60
    secondes = time % 60
    minutes = str(minutes) if minutes >= 10 else "0" + str(minutes)
    secondes = str(secondes) if secondes >= 10 else "0" + str(secondes)
    return minutes + ":" + secondes


def coordinates_to_pixel(square: tuple):
    """
    Fonction recevant les coordonnées d'une case du plateau sous la
    forme d'un couple d'entiers (ligne, colonne) et renvoyant les
    coordonnées du pixel se trouvant au centre de cette case. Ce calcul
    prend en compte la taille de chaque case, donnée par la variable
    globale taille_case.

    :param tuple square: Coordonnées de la case.
    :return tuple: Coordonnées du pixel au centre de la case.
    """
    i, j = square
    return (i + .5) * SQUARE_SIZE, (j + .5) * SQUARE_SIZE + BAR_HEIGHT


def get_snake_color(index: int, rules: dict):
    """
    Détermine la couleur du serpent en fonction de son indice dans la liste des serpents.
    :param int index:Indice dans la liste des serpents.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return tuple: Couleur des remplissage et couleur de contour

    >>> get_snake_color(0, {"invincible": False})
    ('green', 'darkgreen')
    """
    if not rules["invincible"]:
        if index == 0:
            return "green", "darkgreen"
        elif index == 1:
            return "blue", "darkblue"
    return COLORS[index % len(COLORS)], OUTLINE_COLORS[index % len(OUTLINE_COLORS)]


def is_eating_itself(snake: list, invincible: bool):
    """
    Détermine si le serpent se mange lui-même.
    :param list snake: Serpent.
    :param bool invincible: Le serpent est invincible.
    :return bool: Le serpent se mange.

    >>> is_eating_itself([(0, 0), (0, 1), (0, 0)], False)
    True
    """
    i = 0
    while not invincible and i < len(snake) - 1:
        if snake[i] == snake[-1]:
            return True
        i += 1
    return False


def display_apples(apples: list):
    """
    Dessine des pommes à partir d'une liste de couple de coordonées.
    :param list apples: Liste de couples.
    """

    i = 0
    while i < len(apples):
        x, y = coordinates_to_pixel(apples[i])
        cercle(x, y, SQUARE_SIZE / 2, couleur='darkred', remplissage='red')
        cercle(x, y - SQUARE_SIZE / 2, SQUARE_SIZE / 6, couleur='darkgreen', remplissage='green')
        i += 1


def display_cherries(cherries: list):
    """
    Dessine des cerises à partir d'une liste de couple de coordonées.
    :param list cherries: Liste de couples.
    """
    i = 0
    while i < len(cherries):
        x, y = coordinates_to_pixel(cherries[i])
        ligne(x, y - SQUARE_SIZE / 2, x - 2 * SQUARE_SIZE / 6, y + 2 * SQUARE_SIZE / 6, couleur='brown')
        ligne(x, y - SQUARE_SIZE / 2, x + 2 * SQUARE_SIZE / 6, y + 2 * SQUARE_SIZE / 6, couleur='brown')
        cercle(x - 2 * SQUARE_SIZE / 6, y + 2 * SQUARE_SIZE / 6, SQUARE_SIZE / 3.5,
               couleur='darkred', remplissage='red')
        cercle(x + 2 * SQUARE_SIZE / 6, y + 2 * SQUARE_SIZE / 6, SQUARE_SIZE / 3.5,
               couleur='darkred', remplissage='red')
        cercle(x, y - SQUARE_SIZE / 2, SQUARE_SIZE / 6,
               couleur='darkgreen', remplissage='green')
        i += 1


def display_obstacles(obstacles: list):
    """
    Dessine des obstacles à partir d'une liste de couple de coordonées.
    :param list obstacles: Liste de couples.
    """
    i = 0
    while i < len(obstacles):
        x, y = coordinates_to_pixel(obstacles[i])
        rectangle(x - SQUARE_SIZE / 2, y - SQUARE_SIZE / 2, x + SQUARE_SIZE / 2, y + SQUARE_SIZE / 2,
                  remplissage='gray')
        i += 1


def display_bombs(bombs: list, rules: dict):
    """
    Dessine des bombes à partir d'une liste de couple de coordonées.
    :param list bombs: Liste de couples.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    """
    i = 0
    while i < len(bombs):
        x, y = coordinates_to_pixel(bombs[i])
        cercle(x, y, SQUARE_SIZE / 2, couleur='#2c3e50', remplissage='#34495e')
        rectangle(x - 2, y - SQUARE_SIZE * .4, x + 2, y - SQUARE_SIZE * .7, couleur='#2c3e50', remplissage='#34495e')
        texte(x, y, str(rules["bomb_damage"] * rules["framerate"] // START_FRAMERATE), couleur='white',
              ancrage='center', taille=2 * SQUARE_SIZE // 3)
        i += 1


def display_bonuses(bonus: list, type_bonus: int):
    """
    Dessine des bonus à partir d'une liste de couples de coordonées.
    :param bonus: (lst) Liste de couples.
    :param int type_bonus: Type de bonus (0 = étoile, 1 = torique, 2 = vitesse et 3 = mangeur de bombes).
    """
    i = 0
    while i < len(bonus):
        x, y = coordinates_to_pixel(bonus[i])
        if type_bonus == 0:  # Étoile

            mesure = sqrt(2) / 2 * SQUARE_SIZE / 2
            ligne(x - SQUARE_SIZE / 2, y, x + SQUARE_SIZE / 2, y, epaisseur=SQUARE_SIZE / 7, couleur='gold')
            ligne(x, y - SQUARE_SIZE / 2, x, y + SQUARE_SIZE / 2, epaisseur=SQUARE_SIZE / 7, couleur='gold')
            ligne(x - mesure, y - mesure, x + mesure, y + mesure, epaisseur=SQUARE_SIZE / 7, couleur='gold')
            ligne(x + mesure, y - mesure, x - mesure, y + mesure, epaisseur=SQUARE_SIZE / 7, couleur='gold')
            cercle(x, y, 3 * SQUARE_SIZE / 4, epaisseur=SQUARE_SIZE / 7, couleur='orange')

        elif type_bonus == 1:  # Torique

            texte(x, y, 'T', couleur='magenta', ancrage='center', taille=2 * SQUARE_SIZE // 3)
            cercle(x, y, SQUARE_SIZE / 2, epaisseur=SQUARE_SIZE / 7, couleur='darkmagenta')

        elif type_bonus == 2:  # Vitesse

            polygone([(x - 2 * SQUARE_SIZE / 5, y - SQUARE_SIZE / 4), (x, y),
                      (x - 2 * SQUARE_SIZE / 5, y + SQUARE_SIZE / 4)],
                     remplissage='teal', couleur='teal')
            polygone([(x, y - SQUARE_SIZE / 4), (x + 2 * SQUARE_SIZE / 5, y), (x, y + SQUARE_SIZE / 4)],
                     remplissage='teal',
                     couleur='teal')
            cercle(x, y, SQUARE_SIZE / 2, epaisseur=SQUARE_SIZE / 7, couleur='darkslategray')

        elif type_bonus == 3:  # Mangeur de bombes

            rectangle(x - SQUARE_SIZE / 8, y - SQUARE_SIZE / 4, x + SQUARE_SIZE / 8, y + SQUARE_SIZE / 4,
                      remplissage='red', couleur='red')
            rectangle(x - SQUARE_SIZE / 4, y - SQUARE_SIZE / 8, x + SQUARE_SIZE / 4, y + SQUARE_SIZE / 8,
                      remplissage='red', couleur='red')
            cercle(x, y, SQUARE_SIZE / 2, epaisseur=SQUARE_SIZE / 7, couleur='darkred')

        i += 1


def check_apple(snake: list, snake_index: int):
    """
    Vérifie si une pomme a été mangée et incrémente le score le cas échéant.
    :param list snake: Serpent.
    :param int snake_index: Indice du serpent.
    """
    j = 0
    while j < len(apples):
        if snake[-1] == apples[j]:  # La tête du serpent passe sur une pomme.
            x_pomme, y_pomme = apples.pop(j)  # Effacement de la pomme.

            # Ajout d'un élément au corps du serpent.
            snake.insert(0, (x_pomme - direction[snake_index][0], y_pomme - direction[snake_index][1]))
        j += 1


def check_cherry(snake: list, snake_index: int):
    """
    Vérifie si des cerises ont été mangées et incrémente le score le cas échéant.
    :param list snake: Serpent.
    :param int snake_index: Indice du serpent.
    """
    j = 0
    while j < len(cherries):
        if snake[-1] == cherries[j]:  # La tête du serpent passe sur une grappe de cerises.
            x_cerise, y_cerise = cherries.pop(j)  # Effacement des cerises.

            # Ajout de trois éléments au corps du serpent.
            points = 0
            while points < 3:
                snake.insert(0, (x_cerise - direction[snake_index][0], y_cerise - direction[snake_index][1]))
                points += 1
        j += 1


def check_bomb(snake: list, snake_index: int, rules: dict):
    """
    Vérifie si une bombe a été mangé et adapte le score le cas échéant.
    :param list snake: Serpent.
    :param int snake_index: Indice du serpent.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return bool: Booléen déterminant si le jeu doit continuer.
    """
    j = 0
    while j < len(bombs):
        if snake[-1] == bombs[j]:  # La tête du serpent passe sur une bombe.
            x_bombe, y_bombe = bombs.pop(j)  # Effacement de la bombe.

            # Retrait de deux éléments au corps du serpent.
            malus = 0
            while not rules["invincible"] and malus < rules["bomb_damage"] * rules["framerate"] // START_FRAMERATE:
                if len(snake) == 1:  # Il ne reste plus que la tête, défaite.
                    return False
                if not rules["eat_bombs"]:
                    snake.pop(0)
                else:
                    snake.insert(0, (x_bombe - direction[snake_index][0], y_bombe - direction[snake_index][1]))
                malus += 1
        j += 1
    return True


def check_bonus(snake: list, rules: dict):
    """
    Vérifie si un bonus a été mangé et met à jour les règles le cas échéant.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :param list snake: Serpent.
    """
    j = 0
    while j < len(bonuses):
        if snake[-1] == bonuses[j]:
            bonuses.pop(j)

            if rules["bonus_type"] == 0:
                rules["invincible"] = True
                rules["toric"] = True
                rules["framerate"] *= 2
                rules["bonus_duration"] = 10
            elif rules["bonus_type"] == 1:
                rules["toric"] = not rules["toric"]
                rules["bomb_duration"] = 15
            elif rules["bonus_type"] == 2:
                rules["framerate"] *= 2
                rules["bonus_duration"] = 15
            elif rules["bonus_type"] == 3:
                rules["eat_bombs"] = True
                rules["bonus_duration"] = 20

            rules["bonus_activation"] = rules["count"]

        j += 1


def set_looser(index: int, rules: dict):
    """
    Définir le perdant
    :param int index: Identifiant du serpent perdant.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return:
    """
    if index == 0:
        rules["multi_looser"] = "vert"
    elif index == 1:
        rules["multi_looser"] = "bleu"


def display_snakes_and_check(snakes: list, rules: dict):
    """
    Dessine des serpents à partir d'une liste et vérifie les conditions d'échec.
    :param list snakes: Liste de liste de couples.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return bool: Booléen déterminant si le jeu peut continuer.
    """
    s = 0
    while s < len(snakes):
        snake = snakes[s]

        color, outline_color = get_snake_color(s, rules)

        # Animation du déplacement du serpent.
        snake.append((snake[-1][0] + direction[s][0], snake[-1][1] + direction[s][1]))
        if solo:
            snake.pop(0)

        if rules["toric"]:  # L'arène est torique.
            if snake[-1][0] < 0:
                snake[-1] = BOARD_WIDTH - 1, snake[-1][1]
            if snake[-1][0] > BOARD_WIDTH - 1:
                snake[-1] = 0, snake[-1][1]
            if snake[-1][1] < 0:
                snake[-1] = snake[-1][0], BOARD_HEIGHT - 1
            if snake[-1][1] > BOARD_HEIGHT - 1:
                snake[-1] = snake[-1][0], 0
        elif not 0 <= snake[-1][0] < BOARD_WIDTH or not 0 <= snake[-1][1] < BOARD_HEIGHT:  # Le serpent heurte un mur.
            set_looser(s, rules)
            return False

        if is_eating_itself(snake, rules["invincible"]):
            set_looser(s, rules)
            return False

        i = 0
        while i < len(snake):

            if i == len(snake) - 1:
                if solo:
                    check_apple(snake, s)
                    check_cherry(snake, s)
                    if not check_bomb(snake, s, rules):
                        return False
                    check_bonus(snake, rules)
                else:
                    if snake[i] in snakes[s - 1]:  # Un des deux serpents a heurté l'autre.
                        set_looser(s, rules)
                        return False

            # Si la liste a été modifié, l'itération ne doit pas dépasser la nouvelle limite.
            if i > len(snake) - 1:
                break

            if rules["invincible"]:
                color = COLORS[i % len(COLORS)]
                outline_color = OUTLINE_COLORS[i % len(OUTLINE_COLORS)]

            x, y = coordinates_to_pixel(snake[i])
            if i < len(snake) - 1:
                cercle(x, y, SQUARE_SIZE / 2.1, couleur=outline_color, remplissage=color)
            else:
                display_snake_head(x, y, s, i, direction[s], rules)

                if rules["generating_obstacles"] and snake[i] in obstacles and not rules["invincible"]:
                    return False

            i += 1

        s += 1

    return True


def display_snake_head(x: int, y: int, snake_index: int, snake_length: int, direction: tuple, rules: dict):
    """
    Dessine la tête du serpent dans la bonne direction.
    :param int x: Abscisse de la case.
    :param int y: Ordonée de la case.
    :param int snake_index: Indice du serpent.
    :param int snake_length: Taille du serpent.
    :param tuple direction: Direction du serpent.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    """

    if not rules["invincible"]:
        color, outline_color = get_snake_color(snake_index, rules)
    else:
        color, outline_color = COLORS[snake_length % len(COLORS)], OUTLINE_COLORS[snake_length % len(OUTLINE_COLORS)]

    if direction == (1, 0):
        ligne(x + SQUARE_SIZE / 2, y, x + 4 * SQUARE_SIZE / 5, y, couleur='darkred',
              epaisseur=SQUARE_SIZE / 10)
        cercle(x, y, SQUARE_SIZE / 2 + 1, couleur=outline_color, remplissage=color)
        cercle(x + SQUARE_SIZE / 5, y - SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
        cercle(x + SQUARE_SIZE / 5, y + SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
    elif direction == (-1, 0):
        ligne(x - SQUARE_SIZE / 2, y, x - 4 * SQUARE_SIZE / 5, y, couleur='darkred',
              epaisseur=SQUARE_SIZE / 10)
        cercle(x, y, SQUARE_SIZE / 2 + 1, couleur=outline_color, remplissage=color)
        cercle(x - SQUARE_SIZE / 5, y - SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
        cercle(x - SQUARE_SIZE / 5, y + SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
    elif direction == (0, 1):
        ligne(x, y + SQUARE_SIZE / 2, x, y + 4 * SQUARE_SIZE / 5, couleur='darkred',
              epaisseur=SQUARE_SIZE / 10)
        cercle(x, y, SQUARE_SIZE / 2 + 1, couleur=outline_color, remplissage=color)
        cercle(x - SQUARE_SIZE / 5, y + SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
        cercle(x + SQUARE_SIZE / 5, y + SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
    elif direction == (0, -1):
        ligne(x, y - SQUARE_SIZE / 2, x, y - 4 * SQUARE_SIZE / 5, couleur='darkred',
              epaisseur=SQUARE_SIZE / 10)
        cercle(x, y, SQUARE_SIZE / 2 + 1, couleur=outline_color, remplissage=color)
        cercle(x - SQUARE_SIZE / 5, y - SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')
        cercle(x + SQUARE_SIZE / 5, y - SQUARE_SIZE / 5, SQUARE_SIZE / 10, couleur='white',
               remplissage='black')


def change_direction(direction: list, touche: str):
    """
    Définit la nouvelle direction en fonction de la touche pressée.
    :param list direction: Directions actuelles des serpents.
    :param str touche: Touche pressée.
    :return tuple: Nouvelle direction.
    """
    if touche == 'Up':
        if direction[0] == (0, 1):
            return direction[0]
        return 0, -1
    elif touche == 'Down':
        if direction[0] == (0, -1):
            return direction[0]
        return 0, 1
    elif touche == 'Left':
        if direction[0] == (1, 0):
            return direction[0]
        return -1, 0
    elif touche == 'Right':
        if direction[0] == (-1, 0):
            return direction[0]
        return 1, 0
    if touche == 'z' or touche == 'Z':
        if direction[1] == (0, 1):
            return direction[1]
        return 0, -1
    elif touche == 's' or touche == 'S':
        if direction[1] == (0, -1):
            return direction[1]
        return 0, 1
    elif touche == 'q' or touche == 'Q':
        if direction[1] == (1, 0):
            return direction[1]
        return -1, 0
    elif touche == 'd' or touche == 'D':
        if direction[1] == (-1, 0):
            return direction[1]
        return 1, 0
    else:
        return None


def display_texts(rules: dict):
    """
    Affiche tous les textes nécessaires.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    """
    rectangle(0, 0, BOARD_WIDTH * SQUARE_SIZE, BAR_HEIGHT, remplissage='black')
    rectangle(0, BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT, BOARD_WIDTH * SQUARE_SIZE,
              2 * BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT, remplissage='black')
    rectangle(0, BAR_HEIGHT, BOARD_WIDTH * SQUARE_SIZE - 1, BOARD_HEIGHT * SQUARE_SIZE + BAR_HEIGHT - 1)
    texte(5, 5, "Score : " + str(get_score()), couleur='white', tag='score')
    texte(BOARD_WIDTH * SQUARE_SIZE - 5, 5, "Temps : " + format_time(get_time(rules["framerate"], rules)), ancrage='ne',
          couleur='white', tag='temps')
    if rules["evolutive_speed"]:
        texte(BOARD_WIDTH * SQUARE_SIZE / 2, 5, "Vitesse : " + str(rules["framerate"] / START_FRAMERATE) + "x",
              ancrage='n', couleur='white', tag='vitesse')


def display_objects(rules: dict):
    """
    Affiche tous les objets.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    """
    if solo:
        display_apples(apples)
        display_cherries(cherries)
        display_obstacles(obstacles)
        display_bombs(bombs, rules)
        display_bonuses(bonuses, rules["bonus_type"])


def set_solo():
    """
    Demande à l'utilisateur s'il veut jouer seul ou à plusieurs.
    :return bool: Le jeu se déroule en solo.
    """
    solo = input("Dans quel mode souhaitez-vous jouer ? (solo/multi) ")
    while solo.lower() != "solo" and solo.lower() != "multi":
        solo = input("Dans quel mode souhaitez-vous jouer ? (solo/multi) ")
    return solo.lower() == "solo"


def set_toric():
    """
    Demande à l'utilisateur s'il veut jouer dans une arène torique.
    :return bool: L'arène est torique.
    """
    toric = input("Souhaitez-vous jouer dans une arène torique ? (o/n) ")
    while toric.lower() != "o" and toric.lower() != "n":
        toric = input("Souhaitez-vous jouer dans une arène torique ? (o/n) ")
    return toric.lower() == "o"


def set_evolutive_speed():
    """
    Demande à l'utilisateur s'il veut que la vitesse augmente au cours tu temps.
    :return bool: La vitesse augmente au cours du temps.
    """
    evolutive_speed = input("Souhaitez-vous que le jeu accelère au cours du temps ? (o/n) ")
    while evolutive_speed.lower() != "o" and evolutive_speed.lower() != "n":
        evolutive_speed = input("Souhaitez-vous que le jeu accelère au cours du temps ? (o/n) ")
    return evolutive_speed.lower() == "o"


def set_generating_obstacles():
    """
    Demande à l'utilisateur s'il veut jouer avec des obstacles.
    :return bool: Jouer avec des obstacles.
    """
    generating_obstacles = input("Souhaitez-vous que le jeu génère des obstacles ? (o/n) ")
    while generating_obstacles.lower() != "o" and generating_obstacles.lower() != "n":
        generating_obstacles = input("Souhaitez-vous que le jeu génère des obstacles ? (o/n) ")
    return generating_obstacles.lower() == "o"


def set_generating_bonuses():
    """
    Demande à l'utilisateur s'il veut jouer avec des bonus.
    :return bool: Jouer avec des bonus.
    """
    generating_bonuses = input("Souhaitez-vous que le jeu génère des bonus/malus ? (o/n) ")
    while generating_bonuses.lower() != "o" and generating_bonuses.lower() != "n":
        generating_bonuses = input("Souhaitez-vous que le jeu génère des bonus/malus ? (o/n) ")
    return generating_bonuses.lower() == "o"


def generate_apple(apples: list):
    """
    Génère une nouvelle pomme si la dernière a été mangée.
    :param list apples: Liste des pommes.
    """
    if len(apples) == 0:
        x_pomme, y_pomme = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)
        while (x_pomme, y_pomme) in snakes[0] or (x_pomme, y_pomme) in obstacles or (x_pomme, y_pomme) in cherries or \
                (x_pomme, y_pomme) in bombs or (x_pomme, y_pomme) in bonuses:
            x_pomme, y_pomme = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

        apples.append((x_pomme, y_pomme))


def generate_cherry(cherries: list):
    """
    Génère une nouvelle cerise avec une faible probabilité si la dernière a été mangée.
    :param list cherries: Liste des cerises.
    """
    if len(cherries) == 0 and random() < .005:
        x_cherry, y_cherry = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)
        while (x_cherry, y_cherry) in snakes[0] or (x_cherry, y_cherry) in obstacles or (x_cherry, y_cherry) in apples \
                or (x_cherry, y_cherry) in bombs or (x_cherry, y_cherry) in bonuses:
            x_cherry, y_cherry = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

        cherries.append((x_cherry, y_cherry))


def generate_bomb(bombs: list, rules: dict):
    """
    Génère une nouvelle bombe si la dernière a disparu ou fait disparaitre la bombe
    actuelle si celle-ci a atteint sa durée de vie maximale.
    :param list bombs: Liste des bombes.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return int: Moment de placement de la bombe.
    """
    if len(bombs) == 0:
        if random() < .005:
            x_bombe, y_bombe = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

            while (x_bombe, y_bombe) in snakes[0] or (x_bombe, y_bombe) in obstacles or \
                    (x_bombe, y_bombe) in cherries or (x_bombe, y_bombe) in apples or \
                    (x_bombe, y_bombe) in bonuses:
                x_bombe, y_bombe = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

            bombs.append((x_bombe, y_bombe))
            return rules["count"]
    else:
        if rules["count"] - rules["bomb_placement"] >= rules["bomb_duration"] * rules["framerate"]:
            bombs.pop(0)
    return rules["bomb_placement"]


def generate_obstacle(obstacles: list, rules: dict):
    """
    Génère un nouvel obstacle et supprime le plus ancien si la limite est atteinte.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :param list obstacles: Liste des obstacles.
    """
    if rules["generating_obstacles"] and random() < .05:
        if len(obstacles) < BOARD_HEIGHT * BOARD_WIDTH / 50:
            x_obstacle, y_obstacle = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

            while (x_obstacle, y_obstacle) in snakes[0] or (x_obstacle, y_obstacle) in apples or \
                    (x_obstacle, y_obstacle) in cherries or (x_obstacle, y_obstacle) in bombs or \
                    (x_obstacle, y_obstacle) in bonuses:
                x_obstacle, y_obstacle = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)
            obstacles.append((x_obstacle, y_obstacle))
        else:
            obstacles.pop(0)
            x_obstacle, y_obstacle = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)
            s = 0
            while s < len(snakes):
                serpent = snakes[s]
                while (x_obstacle, y_obstacle) in serpent:
                    x_obstacle, y_obstacle = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)
                s += 1
            obstacles.append((x_obstacle, y_obstacle))


def generate_bonus(bonuses: list, rules: dict):
    """
    Génère un nouveau bonus avec une faible probalité si le dernier a été mangé.
    :param list bonuses: Liste des bonus.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return tuple: Type et durée du bonus.
    """
    if rules["generating_bonuses"] and len(bonuses) == 0 and rules["bonus_type"] == -1:
        if random() < .0075:
            x_bonus, y_bonus = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

            while (x_bonus, y_bonus) in snakes[0] or (x_bonus, y_bonus) in obstacles or \
                    (x_bonus, y_bonus) in cherries or (x_bonus, y_bonus) in apples or \
                    (x_bonus, y_bonus) in bombs:
                x_bonus, y_bonus = randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1)

            if random() < 0.2:
                bonuses.append((x_bonus, y_bonus))
                return 0, 10
            else:
                rand = random()
                if rand < .33:
                    bonuses.append((x_bonus, y_bonus))
                    return 1, 15
                elif rand < .66:
                    bonuses.append((x_bonus, y_bonus))
                    return 2, 15
                else:
                    bonuses.append((x_bonus, y_bonus))
                    return 3, 20
    return rules["bonus_type"], rules["bonus_duration"]


def disable_bonus(rules: dict):
    """
    Désactive un bonus quand ce dernier a atteint sa durée et réinitialise les variables.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return tuple: Options de partie par défaut.
    """
    if rules["count"] - rules["bonus_activation"] >= rules["bonus_duration"] * rules["framerate"]:

        if rules["bonus_type"] == 0:
            rules["framerate"] //= 2
            rules["invincible"] = False
            if not rules["start_toricity"]:
                rules["toric"] = False
            else:
                rules["toric"] = True
        elif rules["bonus_type"] == 1:
            rules["toric"] = not rules["toric"]
        elif rules["bonus_type"] == 2:
            rules["framerate"] //= 2
        elif rules["bonus_type"] == 3:
            rules["eat_bombs"] = False

        rules["bonus_duration"] = -1
        rules["bonus_activation"] = -1
        rules["bonus_type"] = -1
    else:
        display_bonus_text(rules)


def display_bonus_text(rules: dict):
    """
    Affiche le message relatif au bonus en activé.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    """
    if rules["bonus_type"] == 0:
        texte(5, BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT + 5,
              "Bonus : Invincible, arène torique, vitesse x2 (" + format_time(
                  rules["bonus_duration"] - (rules["count"] - rules["bonus_activation"]) // rules["framerate"]) + ")",
              couleur='white',
              ancrage='nw')
    elif rules["bonus_type"] == 1:
        if rules["toric"]:
            texte(5, BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT + 5,
                  "Bonus : Arène torique (" + format_time(
                      rules["bonus_duration"] - (rules["count"] - rules["bonus_activation"]) // rules[
                          "framerate"]) + ")",
                  couleur='white',
                  ancrage='nw')
        else:
            texte(5, BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT + 5,
                  "Malus : Arène non torique (" + format_time(
                      rules["bonus_duration"] - (rules["count"] - rules["bonus_activation"]) // rules[
                          "framerate"]) + ")",
                  couleur='white',
                  ancrage='nw')
    elif rules["bonus_type"] == 2:
        texte(5, BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT + 5,
              "Bonus : Vitesse x2 (" + format_time(
                  rules["bonus_duration"] - (rules["count"] - rules["bonus_activation"]) // rules["framerate"]) + ")",
              couleur='white',
              ancrage='nw')
    elif rules["bonus_type"] == 3:
        texte(5, BAR_HEIGHT + SQUARE_SIZE * BOARD_HEIGHT + 5,
              "Bonus : Mangeur de bombes (" + format_time(
                  rules["bonus_duration"] - (rules["count"] - rules["bonus_activation"]) // rules["framerate"]) + ")",
              couleur='white',
              ancrage='nw')


def increase_speed(rules: dict):
    """
    Augmente la vitesse du jeu.
    :param dict rules: Dictionnaire conetenant les règles actuelles.
    :return int: Nouveau taux de rafraîchissement.
    """
    temps_actuel = get_time(rules["framerate"], rules)
    if rules["evolutive_speed"] and temps_actuel > 0 and temps_actuel % 10 == 0 and rules["framerate"] < 30:
        if not rules["speed_up"]:
            rules["speed_up"] = True
    else:
        if rules["speed_up"]:
            rules["framerate"] += 1
            while get_time(rules["framerate"], rules) < temps_actuel:
                rules["count"] += 1
                rules["speed_up"] = False
    return rules["framerate"]


# Programme principal
if __name__ == "__main__":

    apples = []
    cherries = []
    obstacles = []
    bombs = []
    bonuses = []
    snakes = []

    pause = False

    solo = set_solo()

    rules = {"framerate": START_FRAMERATE,
             "invincible": False,
             "eat_bombs": False,
             "toric": False,
             "start_toricity": False,
             "bonus_activation": -1,
             "bonus_type": -1,
             "bonus_duration": -1,
             "bomb_placement": -1,
             "bomb_duration": 10,
             "bomb_damage": 10,
             "evolutive_speed": False,
             "generating_obstacles": False,
             "generating_bonuses": False,
             "multi_looser": None,
             "speed_up": False,
             "count": 0}

    testmod()

    if solo:
        snakes.append([(BOARD_WIDTH // 2, BOARD_HEIGHT // 2)])  # Définition du point d'apparition du serpent.
        direction = [(1, 0)]  # Direction initiale du serpent. (Vers la droite)

        rules["toric"] = set_toric()
        rules["evolutive_speed"] = set_evolutive_speed()
        rules["generating_obstacles"] = set_generating_obstacles()
        rules["generating_bonuses"] = set_generating_bonuses()
        rules["start_toricity"] = rules["toric"]
    else:
        snakes.append([(BOARD_WIDTH // 4, BOARD_HEIGHT // 2)])  # Initialisation des deux serpents.
        snakes.append([(3 * BOARD_WIDTH // 4, BOARD_HEIGHT // 2)])  #

        direction = [(0, -1), (0, 1)]  # Direction initiale des serpent.

    # Initialisation du jeu
    cree_fenetre(SQUARE_SIZE * BOARD_WIDTH, SQUARE_SIZE * BOARD_HEIGHT + 2 * BAR_HEIGHT)

    # Boucle principale.
    while True:

        # Gestion des événements.
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            break
        elif ty == 'Touche':
            # Mise en pause du jeu ou annulation de la pause.
            if touche(ev) == 'p' or touche(ev) == 'P':
                pause = not pause

            # Modification de la direction du serpent principal. (solo et J1 en multi)
            elif touche(ev) == 'Left' or touche(ev) == 'Right' or touche(ev) == 'Up' or touche(ev) == 'Down':
                direction[0] = change_direction(direction, touche(ev))

            # Modification de la direction du serpent secondaire. (J2 en multi)
            elif touche(ev) == 'z' or touche(ev) == 'q' or touche(ev) == 's' or touche(ev) == 'd' or \
                    touche(ev) == 'Z' or touche(ev) == 'Q' or touche(ev) == 'S' or touche(ev) == 'D':
                direction[1] = change_direction(direction, touche(ev))

        # Vérification de l'état de pause.
        if not pause:
            rules["count"] += 1
            efface_tout()
            display_texts(rules)
            display_objects(rules)
            increase_speed(rules)

            # Vérification que le serpent ne se soit pas mangé lui même.
            if not display_snakes_and_check(snakes, rules):
                break

            if rules["count"] < rules["framerate"] * 3 and rules["count"] % rules["framerate"] < 5:
                # Affichage d'un message les 3 premières secondes.
                texte(BOARD_WIDTH * SQUARE_SIZE / 2, BOARD_HEIGHT * SQUARE_SIZE / 2, "C'est parti !",
                      ancrage='center', taille=32, couleur='blue', tag='texte_debut')

            generate_apple(apples)
            generate_cherry(cherries)
            rules["bomb_placement"] = generate_bomb(bombs, rules)
            generate_obstacle(obstacles, rules)
            rules["bonus_type"], rules["bonus_duration"] = generate_bonus(bonuses, rules)

            if rules["bonus_type"] > -1 and rules["bonus_duration"] > -1:
                rules["bonus_type"] = rules["bonus_type"]
                rules["bomb_duration"] = rules["bonus_duration"]

            if rules["bonus_activation"] > -1:
                disable_bonus(rules)
        else:
            efface('texte_debut')
            efface('score')
            efface('vitesse')
            efface('temps')
            texte(BOARD_WIDTH * SQUARE_SIZE / 2, 5, "PAUSE", ancrage='n', couleur='green', tag='pause')

        # Attente avant rafraîchissement.
        mise_a_jour()
        sleep(1 / rules["framerate"])

    efface_tout()
    if solo:
        texte(BOARD_WIDTH * SQUARE_SIZE // 2, BOARD_HEIGHT * SQUARE_SIZE // 2, "Perdu !", couleur='red',
              ancrage='s', taille=32)
        texte(BOARD_WIDTH * SQUARE_SIZE // 2, BOARD_HEIGHT * SQUARE_SIZE // 2,
              "Votre score : " + str(get_score()), couleur='darkred', ancrage='n',
              taille=24)
    else:
        texte(BOARD_WIDTH * SQUARE_SIZE // 2, BOARD_HEIGHT * SQUARE_SIZE // 2, "Perdu !", couleur='red',
              ancrage='s', taille=32)
        if rules["multi_looser"] is not None:
            texte(BOARD_WIDTH * SQUARE_SIZE // 2, BOARD_HEIGHT * SQUARE_SIZE // 2,
                  "Le serpent " + rules["multi_looser"] + " a perdu", couleur='darkred', ancrage='n', taille=24)
        else:
            texte(BOARD_WIDTH * SQUARE_SIZE // 2, BOARD_HEIGHT * SQUARE_SIZE // 2,
                  "La partie a été arrêtée", couleur='darkred', ancrage='n', taille=24)

    # Fermeture et sortie.
    attend_fermeture()
