import pygame
from settings import *


def ray_casting(screen, player_pos, player_angle):
    cur_angle = player_angle - (FOV / 2)
    xo, yo = player_pos

    for ray in range(NRAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(1, MAX_DEPTH + 1):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            color = 255 / (1 + depth ** 2 * 0.0001)
            # pygame.draw.line(screen, GRAY, player_pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                proj_h = PROJ_COEFF / depth
                pygame.draw.rect(screen, (color // 3, color // 2, color), (ray * SCALE, (HEIGHT // 2) - proj_h // 2, SCALE, proj_h))
                break
        cur_angle += DELTA_ANGLE
