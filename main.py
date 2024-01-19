import math
from drawing import *

import sys

import os
import pygame

from settings import *
from settings import FPS
from player import Player, Weapon
from sprites import *
from rc import *
from interact import *


def start_screen():
    font = pygame.font.SysFont("Verdana", 250)
    fon = pygame.transform.scale(load_image('lobby.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    button = get_component_button(WIDTH // 2, HEIGHT // 2 - 80, 'ИГРАТЬ')
    button2 = get_component_button(WIDTH // 2, HEIGHT // 2 - 10, 'ДОСТИЖЕНИЯ')
    button3 = get_component_button(WIDTH // 2, HEIGHT // 2 + 60, 'НАСТРОЙКИ')
    button4 = get_component_button(WIDTH // 2, HEIGHT // 2 + 130, 'ВЫЙТИ')
    color = (162, 65, 47)
    pygame.draw.rect(screen, color, button[2])
    screen.blit(button[0], button[1])

    pygame.draw.rect(screen, color, button2[2])
    screen.blit(button2[0], button2[1])

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
                        main()
                        return
                    if button2[2].collidepoint(mouse_pos):
                        achievements()
                        return
                    if button3[2].collidepoint(mouse_pos):
                        sattings()
                        return
                    if button4[2].collidepoint(mouse_pos):
                        exit()
        pygame.display.flip()


def sattings():
    global FPS
    font = pygame.font.SysFont("Verdana", 50)
    button1 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2 - 100, '<МАКС FPS>')
    button3 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2, '<ЗВУК>')
    button4 = get_component_button(WIDTH // 2 - 150, HEIGHT // 2 + 100, 'В МЕНЮ')
    color = (162, 65, 47)
    while True:
        screen.fill((0, 0, 0))
        fon = pygame.transform.scale(load_image('settings.jpeg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))

        pygame.draw.rect(screen, color, button1[2])
        screen.blit(button1[0], button1[1])

        pygame.draw.rect(screen, color, button3[2])
        screen.blit(button3[0], button3[1])

        pygame.draw.rect(screen, color, button4[2])
        screen.blit(button4[0], button4[1])

        fps = font.render(f'{FPS}', True, (255, 255, 255))
        screen.blit(fps, (button1[2].x + 360, button1[2].y))
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
                        if FPS > 15:
                            FPS -= 15
                    if button1[4].collidepoint(mouse_pos):
                        FPS += 15
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
                        main()
                    if button1[2].collidepoint(mouse_pos):
                        start_screen()
                        return
        pygame.display.flip()


def win():
    font = pygame.font.SysFont("Verdana", 200)
    screen.fill((86, 86, 86))
    button1 = get_component_button(WIDTH // 2, HEIGHT // 2 + 110, 'В МЕНЮ', 500, 100)
    color = (162, 65, 47)

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])
    win = font.render('ПОБЕДА', True, (255, 204, 0))
    screen.blit(win, ((WIDTH - win.get_rect().width) // 2, 50))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button1[2].collidepoint(mouse_pos):
                        start_screen()
                        return
        pygame.display.flip()


def achievements():
    with open('kills.txt', 'r') as file:
        kills_count = int(file.read())
    with open('deaths.txt', 'r') as file:
        death_count = int(file.read())
    font1 = pygame.font.SysFont("Verdana", 150)
    font2 = pygame.font.SysFont("Verdana", 50)
    screen.fill((86, 86, 86))
    button1 = get_component_button(WIDTH // 2, HEIGHT // 2 + 300, 'В МЕНЮ', 500, 100)
    color = (162, 65, 47)

    pygame.draw.rect(screen, color, button1[2])
    screen.blit(button1[0], button1[1])
    achievement = font1.render('ДОСТИЖЕНИЯ', True, (255, 204, 0))
    screen.blit(achievement, ((WIDTH - achievement.get_rect().width) // 2, 10))

    kills = font2.render(f'Убийства: {kills_count}', True, (255, 204, 0))
    screen.blit(kills, ((WIDTH - kills.get_rect().width) // 2, 400))

    death = font2.render(f'Смерти: {death_count}', True, (255, 204, 0))
    screen.blit(death, ((WIDTH - kills.get_rect().width) // 2, 460))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
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


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    i = 0
    with open('deaths.txt', 'r') as file:
        death_count = int(file.read())
    with open('kills.txt', 'r') as file:
        kills_count = int(file.read())
    drawing = Drawing(screen)
    sprites = Sprites()
    player = Player(ANGLE, sprites)
    all_sprites = pygame.sprite.Group()
    weapon = Weapon(all_sprites)
    interactive = Interact(player, sprites)
    is_shooting = False
    player.helth = 100

    def npc_check(sprites_list, kills):
        for obj in sprites_list:
            if obj.is_active:
                del_x = obj.x - player.pos[0]
                del_y = obj.y - player.pos[1]
                obj.x = obj.x + 1 if del_x < 0 else obj.x - 1
                obj.y = obj.y + 1 if del_y < 0 else obj.y - 1
                player.helth -= 0.05
            if obj.is_dead:
                sprites.list_of_objects.remove(obj)
                kills += 1
                with open('kills.txt', 'w') as f:
                    f.write(str(kills))

    while True:
        if not sprites.list_of_objects:
            win()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pause()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    all_sprites.update(0)
                    is_shooting = True
        interactive.shooting(is_shooting)
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
            death_count += 1
            with open('death.txt', 'w') as f:
                f.write(str(death_count))
            break

        interactive.npc_action()
        npc_check(sprites.list_of_objects, kills_count)

        clock.tick(FPS)
        print(clock.get_fps())

        # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 10)
        # pygame.draw.line(screen, RED, player.pos, (player.x + WIDTH * math.cos(plНayer.angle),
        # player.y + WIDTH * math.sin(player.angle)))
        # for x,y in world_map:
        # pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE), 2)
        pygame.display.flip()
        i += 1


start_screen()