import pygame
from settings import *
from rc import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.textures = {'1': pygame.image.load('textures/wall.png').convert(),
                         '2': pygame.image.load('textures/wall2.png').convert()}

    def draw_background(self):
        pygame.draw.rect(self.sc, BLUE, (0, 0, WIDTH, (HEIGHT // 2)))
        pygame.draw.rect(self.sc, GRAY, (0, (HEIGHT // 2), WIDTH, (HEIGHT // 2)))

    def draw_space(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)
