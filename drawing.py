import pygame
from settings import *
from rc import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.textures = {'1': pygame.image.load('textures/texture.png').convert(),
                         '2': pygame.image.load('textures/texture1.png').convert()}

    def draw_background(self):
        pygame.draw.rect(self.sc, BLUE, (0, 0, WIDTH, (HEIGHT // 2)))
        pygame.draw.rect(self.sc, GRAY, (0, (HEIGHT // 2), WIDTH, (HEIGHT // 2)))

    def draw_space(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)
