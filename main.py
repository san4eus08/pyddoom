import math

import pygame
from settings import *
from player import Player
from rc import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    player.move()
    screen.fill(BLACK)

    #pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 10)
    #pygame.draw.line(screen, RED, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                               #player.y + WIDTH * math.sin(player.angle)))
    #for x,y in world_map:
       # pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE), 2)

    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, (HEIGHT // 2)))
    pygame.draw.rect(screen, GRAY, (0, (HEIGHT // 2), WIDTH, (HEIGHT // 2)))

    ray_casting(screen, player.pos, player.angle)

    pygame.display.flip()
    clock.tick(FPS)
    print(clock.get_fps())

