import math

import pygame
from settings import *


class Player:
    def __init__(self, Angle, sprites):
        self.x, self.y = player_pos
        self.Angle = Angle
        self.angle = player_angle
        self.speed = player_speed
        self.helth = 100
        # коллизия
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.sprites = sprites
        self.collision_sprites = [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in
                                  self.sprites.list_of_objects if obj.not_fake]
        self.collision = collision_walls + self.collision_sprites

    # обалдеть что в питоне есть
    @property
    def pos(self):
        return self.x, self.y

    def check_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hits = next_rect.collidelistall(self.collision)

        if len(hits):
            delta_x, delta_y = 0, 0
            for hit in hits:
                hit_rect = self.collision[hit]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 20:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            dx = self.speed * cos_a
            dy = self.speed * sin_a
            self.check_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -self.speed * cos_a
            dy = -self.speed * sin_a
            self.check_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = self.speed * sin_a
            dy = -self.speed * cos_a
            self.check_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -self.speed * sin_a
            dy = self.speed * cos_a
            self.check_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= self.Angle
        if keys[pygame.K_RIGHT]:
            self.angle += self.Angle

        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI


class Weapon(pygame.sprite.Sprite):
    image = pygame.image.load('Data/gun2.png')
    gun = pygame.image.load('Data/gun2.png')
    shot = pygame.image.load('Data/gun3.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Weapon.image
        self.rect = self.image.get_rect()
        self.rect.x = 660
        self.rect.y = 700

    def update(self, n=0):
        if n % 2 == 0:
            self.image = self.shot
        else:
            self.image = self.gun
