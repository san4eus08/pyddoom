import pygame
from settings import *


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(screen, player_pos, player_angle, textures):
    # cur_angle = player_angle - (FOV / 2)
    # xo, yo = player_pos
    #
    # for ray in range(NRAYS):
    #     sin_a = math.sin(cur_angle)
    #     cos_a = math.cos(cur_angle)
    #     for depth in range(1, MAX_DEPTH + 1):
    #         x = xo + depth * cos_a
    #         y = yo + depth * sin_a
    #         color = 255 / (1 + depth ** 2 * 0.0001)
    #         # pygame.draw.line(screen, GRAY, player_pos, (x, y), 2)
    #         if (x // TILE * TILE, y // TILE * TILE) in world_map:
    #             proj_h = PROJ_COEFF / depth
    #             pygame.draw.rect(screen, (color // 3, color // 2, color), (ray * SCALE, (HEIGHT // 2) - proj_h // 2, SCALE, proj_h))
    #             break
    #     cur_angle += DELTA_ANGLE

    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - (FOV / 2)
    depth_v = 0
    depth_h = 0
    for ray in range(NRAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        if cos_a >= 0:
            x = xm + TILE
            dx = 1
        else:
            x = xm
            dx = -1

        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        if sin_a >= 0:
            y = ym + TILE
            dy = 1
        else:
            y = ym
            dy = -1

        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        depth *= math.cos(player_angle - cur_angle)
        offset = int(offset) % TILE
        depth = max(depth, 0.0000000000001)
        proj_h = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
        # это покраска одной части стены
        wall_c = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_H)
        wall_c = pygame.transform.scale(wall_c, (SCALE, proj_h))
        screen.blit(wall_c, (ray * SCALE, (HEIGHT//2) - proj_h // 2))

        cur_angle += DELTA_ANGLE
