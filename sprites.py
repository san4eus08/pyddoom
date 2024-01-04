import math

import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprites_types = {
            'monster': pygame.image.load('textures/texture.png').convert_alpha()
        }
        self.list_of_objects = [
            SpriteObject(self.sprites_types['monster'], True, (5, 5), 1, 0.4)
        ]


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale

    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        # ура геометрия опять помогла
        dist = math.sqrt(dx ** 2 + dy ** 2)

        # дальше бога нет....
        theta = math.atan2(dy, dy)
        gamma = theta - player.angle
        if (dx > 0 and 180 <= math.degrees(player.angle) <= 360) or (dx < 0 and dy < 0):
            gamma += D_PI

        drays = int(gamma / DELTA_ANGLE)
        curr_ray = C_RAY + drays
        dist *= math.cos((FOV // 2) - curr_ray * DELTA_ANGLE)

        if 0 <= curr_ray <= NRAYS - 1 and dist < walls[curr_ray][0]:
            proj_height = int(PROJ_COEFF / dist * self.scale)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            sprite_pos = (curr_ray * SCALE - half_proj_height, (HEIGHT // 2) - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))

            return (dist, sprite, sprite_pos)
        return (False, )

