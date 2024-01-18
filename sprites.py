import math

import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprites_params = {
            'monster': {
                'sprite': pygame.image.load('textures/mobe1.png').convert_alpha(),
                'static': True,
                'shift': 0,
                'scale': 1,
                'not_fake': True,
                'type': 'npc',
                'is_dead': False
            },
            'light': {
                'sprite': pygame.image.load('textures/light2.png').convert_alpha(),
                'static': True,
                'shift': -1,
                'scale': 1,
                'not_fake': False,
                'type': 'decor',
                'is_dead': 'None'
            }
        }
        self.list_of_objects = [
            SpriteObject(self.sprites_params['monster'], (6, 6)),
            SpriteObject(self.sprites_params['light'], (9, 8))
        ]

    @property
    def sprite_shot(self):
        return min([obj.is_on_fire for obj in self.list_of_objects], default=(float('inf'), 0))


class SpriteObject:
    def __init__(self, params, pos):
        self.object = params['sprite']
        self.static = params['static']
        self.shift = params['shift']
        self.scale = params['scale']
        self.not_fake = params['not_fake']
        self.type = params['type']
        self.is_dead = params['is_dead']
        self.side = 30
        self.x, self.y = pos[0] * TILE, pos[1] * TILE

    @property
    def is_on_fire(self):
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.not_fake:
            return self.distance_to_sprite, self.proj_height
        return float('inf'), None

    @property
    def pos(self):
        return self.x - self.side // 2, self.y - self.side // 2

    # дальше бога нет...
    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for i in range(FAKE_RAYS)]
        fake_walls1 = [walls[-1] for i in range(FAKE_RAYS)]
        fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        self.current_ray = CENTER_RAY + delta_rays
        self.distance_to_sprite *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS
        if 0 <= fake_ray <= NRAYS - 1 + 2 * FAKE_RAYS and self.distance_to_sprite < fake_walls[fake_ray][0]:
            self.proj_height = min(int(PROJ_COEFF / self.distance_to_sprite * self.scale), 2 * HEIGHT)
            half_proj_height = self.proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if self.theta < 0:
                    self.theta += DOUBLE_PI
                self.theta = 360 - int(math.degrees(self.theta))

                for angles in self.sprite_angles:
                    if self.theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_pos = (self.current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (self.proj_height, self.proj_height))
            return (self.distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)

