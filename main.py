import math
from drawing import Drawing

import sys

import os
import pygame

import settings
from settings import *
from settings import FPS
from player import Player, Weapon
from sprites import *
from rc import *


def start_screen():
    font = pygame.font.SysFont("Verdana", 250)
    fon = pygame.transform.scale(load_image('lobby.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    button = get_component_button(WIDTH // 2, HEIGHT // 2 - 100, 'ИГРАТЬ')
    button1 = get_component_button(WIDTH // 2, HEIGHT // 2 - 30, 'УРОВНИ')
    button3 = get_component_button(WIDTH // 2, HEIGHT // 2 + 40, 'НАСТРОЙКИ')
    button4 = get_component_button(WIDTH // 2, HEIGHT // 2 + 110, 'ВЫЙТИ')
    color = (162, 65, 47)
    pygame.draw.rect(screen, color, button[2])
    screen.blit(button[0], button[1])

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])

    pygame.draw.rect(screen, color, button3[2])
    screen.blit(button3[0], button3[1])

    pygame.draw.rect(screen, color, button4[2])
    screen.blit(button4[0], button4[1])

    doom = font.render('DOOM', True, (255, 204, 0))
    screen.blit(doom, (WIDTH // 2 - 400, 10))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        return
                    if button1[2].collidepoint(mouse_pos):
                        levels()
                        return
                    if button3[2].collidepoint(mouse_pos):
                        sattings()
                        return
                    if button4[2].collidepoint(mouse_pos):
                        exit()
        pygame.display.flip()


def sattings():
    font = pygame.font.SysFont("Verdana", 50)
    button1 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2 - 150, '<МАКС FPS>')
    button2 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2 - 50, '<ЧУВСТВ.>')
    button3 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2 + 50, '<ЗВУК>')
    button4 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2 + 150, 'В МЕНЮ')
    color = (162, 65, 47)
    while True:
        screen.fill((0, 0, 0))
        fon = pygame.transform.scale(load_image('settings.jpeg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))

        pygame.draw.rect(screen, color, button1[2])
        screen.blit(button1[0], button1[1])

        pygame.draw.rect(screen, color, button2[2])
        screen.blit(button2[0], button2[1])

        pygame.draw.rect(screen, color, button3[2])
        screen.blit(button3[0], button3[1])

        pygame.draw.rect(screen, color, button4[2])
        screen.blit(button4[0], button4[1])

        fps = font.render(f'{settings.FPS}', True, (255, 255, 255))
        screen.blit(fps, (button1[2].x + 360, button1[2].y))

        angle = font.render(f'{round(settings.ANGLE, 2) * 100}', True, (255, 255, 255))
        screen.blit(angle, (button2[2].x + 360, button2[2].y))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button1[3].collidepoint(mouse_pos):
                        if settings.FPS > 15:
                            settings.FPS -= 15
                    if button1[4].collidepoint(mouse_pos):
                        settings.FPS += 15
                    if button2[3].collidepoint(mouse_pos):
                        if settings.ANGLE > 0.01:
                            settings.ANGLE -= 0.01
                    if button2[4].collidepoint(mouse_pos):
                        settings.ANGLE += 0.01
                    if button4[2].collidepoint(mouse_pos):
                        start_screen()
                        return

        pygame.display.flip()


def pause():
    screen.fill((86, 86, 86))
    button = get_component_button(WIDTH // 2, HEIGHT // 2 - 70, 'ПРОДОЛЖИТЬ')
    button1 = get_component_button(WIDTH // 2, HEIGHT // 2, 'НАСТРОЙКИ')
    button2 = get_component_button(WIDTH // 2, HEIGHT // 2 + 70, 'В МЕНЮ')
    color = (162, 65, 47)
    pygame.draw.rect(screen, color, button[2])
    screen.blit(button[0], button[1])

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])

    pygame.draw.rect(screen, color, button2[2])
    screen.blit(button2[0], button2[1])

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        return
                    if button1[2].collidepoint(mouse_pos):
                        sattings()
                        return
                    if button2[2].collidepoint(mouse_pos):
                        start_screen()
                        return
        pygame.display.flip()


def levels():
    fon = pygame.transform.scale(load_image('levels.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    button = get_component_button(WIDTH // 4, HEIGHT // 2 - 100, '', 200, 200)
    button1 = get_component_button(WIDTH // 2 - 100, HEIGHT // 2 - 100, '', 200, 200)
    button2 = get_component_button(WIDTH // 4, HEIGHT // 2 + 150, '', 200, 200)
    button3 = get_component_button(WIDTH // 2 - 100, HEIGHT // 2 + 150, '', 200, 200)
    button4 = get_component_button(WIDTH // 2 + 250, HEIGHT // 2 + 25, '', 300, 300)
    button5 = get_component_button(10, 10, '', 50, 50)
    color = (162, 65, 47)
    pygame.draw.rect(screen, color, button[2])
    screen.blit(button[0], button[1])

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])

    pygame.draw.rect(screen, color, button2[2])
    screen.blit(button2[0], button2[1])

    pygame.draw.rect(screen, color, button3[2])
    screen.blit(button3[0], button3[1])

    pygame.draw.rect(screen, color, button4[2])
    screen.blit(button4[0], button4[1])

    pygame.draw.rect(screen, color, button5[2])
    pygame.draw.line(screen, (255, 204, 0), (button5[2].x, button5[2].y), (button5[2].x + button5[2].w,
                                                                           button5[2].y + button5[2].h))
    pygame.draw.line(screen, (255, 204, 0), (button5[2].x + button5[2].w, button5[2].y), (button5[2].x,
                                                                                          button5[2].y + button5[2].h))
    screen.blit(button5[0], button5[1])
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        pass
                    if button1[2].collidepoint(mouse_pos):
                        pass
                    if button2[2].collidepoint(mouse_pos):
                        pass
                    if button5[2].collidepoint(mouse_pos):
                        start_screen()
                        return
            pygame.display.flip()


def defeat():
    font = pygame.font.SysFont("Verdana", 200)
    screen.fill((86, 86, 86))
    button = get_component_button(WIDTH // 2, HEIGHT // 2, 'ЗАНОВО', 500, 100)
    button1 = get_component_button(WIDTH // 2, HEIGHT // 2 + 110, 'В МЕНЮ', 500, 100)
    color = (162, 65, 47)
    pygame.draw.rect(screen, color, button[2])
    screen.blit(button[0], button[1])

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])
    doom = font.render('ВЫ УМЕРЛИ', True, (255, 204, 0))
    screen.blit(doom, (WIDTH // 2 - 600, 50))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button[2].collidepoint(mouse_pos):
                        return
                    if button1[2].collidepoint(mouse_pos):
                        start_screen()
                        return
        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def get_component_button(button_x, button_y, text='', button_width=300, button_height=60):
    font = pygame.font.Font(None, 50)
    text_surface = font.render(text, True, (255, 204, 0))

    button_rect = pygame.Rect(button_x - button_width // 2, button_y - button_height // 2, button_width, button_height)
    button_up_rect = pygame.Rect(button_x - button_width // 2, button_y - button_height // 2, button_width // 2,
                                 button_height)
    button_down_rect = pygame.Rect(button_x, button_y - button_height // 2, button_width // 2,
                                   button_height)

    text_rect = text_surface.get_rect(center=button_rect.center)

    return text_surface, text_rect, button_rect, button_up_rect, button_down_rect


def npc_check(sprites_list):
    for obj in sprites_list:
        if obj.is_active:
            del_x = sprt.x - player.pos[0]
            del_y = sprt.y - player.pos[1]
            sprt.x = sprt.x + 1 if del_x < 0 else sprt.x - 1
            sprt.y = sprt.y + 1 if del_y < 0 else sprt.y - 1
            player.helth -= 0.05


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
start_screen()
drawing = Drawing(screen)
sprites = Sprites()
player = Player(settings.ANGLE, sprites)
all_sprites = pygame.sprite.Group()
weapon = Weapon(all_sprites)
i = 0
is_shooting = False
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pause()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                all_sprites.update(0)
                is_shooting = True
    if i % 10 == 0:
        all_sprites.update(1)
        is_shooting = False
    screen.fill(BLACK)
    player.move()
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, (HEIGHT // 2)))
    pygame.draw.rect(screen, GRAY, (0, (HEIGHT // 2), WIDTH, (HEIGHT // 2)))

    drawing.draw_background()

    walls, wall_shot = ray_casting_walls(player, drawing.textures)
    drawing.draw_space(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])

    all_sprites.draw(screen)
    if player.helth > 0:
        pygame.draw.rect(screen, RED, (20, HEIGHT - 60, player.helth * 4, 40))
    else:
        defeat()
        player.helth = 100

    clock.tick(settings.FPS)
    print(clock.get_fps())

    # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 10)
    # pygame.draw.line(screen, RED, player.pos, (player.x + WIDTH * math.cos(plНayer.angle),
    # player.y + WIDTH * math.sin(player.angle)))
    # for x,y in world_map:
    # pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE), 2)
    pygame.display.flip()
    i += 1
