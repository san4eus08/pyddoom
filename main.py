import math

import  sys

import os
import pygame
from settings import *
from player import Player
from rc import *


def start_screen():
    fon = pygame.transform.scale(load_image('lobby.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    button = get_component_button(WIDTH // 2, HEIGHT // 2 - 140,'ИГРАТЬ')
    button1 = get_component_button(WIDTH // 2, HEIGHT // 2 - 70,'УРОВНИ')
    button2 = get_component_button(WIDTH // 2, HEIGHT // 2, 'ОРУЖИЕ')
    button3 = get_component_button(WIDTH // 2, HEIGHT // 2 + 70, 'НАСТРОЙКИ')
    color = (162, 65, 47)
    pygame.draw.rect(screen, color, button[2])
    screen.blit(button[0], button[1])

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])

    pygame.draw.rect(screen, color, button2[2])
    screen.blit(button2[0], button2[1])

    pygame.draw.rect(screen, color, button3[2])
    screen.blit(button3[0], button3[1])

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        return
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button1[2].collidepoint(mouse_pos):
                        pygame.quit()
        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def get_component_button(button_x, button_y, text):
    font = pygame.font.Font(None, 50)
    text_surface = font.render(text, True, (255, 204, 0))

    button_width = 300
    button_height = 60

    button_rect = pygame.Rect(button_x - button_width // 2, button_y - button_height // 2, button_width, button_height)

    text_rect = text_surface.get_rect(center=button_rect.center)

    return text_surface, text_rect, button_rect


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
start_screen()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    screen.fill(BLACK)
    player.move()
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, (HEIGHT // 2)))
    pygame.draw.rect(screen, GRAY, (0, (HEIGHT // 2), WIDTH, (HEIGHT // 2)))

    ray_casting(screen, player.pos, player.angle)
    clock.tick(FPS)
    print(clock.get_fps())

    # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 10)
    # pygame.draw.line(screen, RED, player.pos, (player.x + WIDTH * math.cos(plНayer.angle),
    # player.y + WIDTH * math.sin(player.angle)))
    # for x,y in world_map:
    # pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE), 2)
    pygame.display.flip()
