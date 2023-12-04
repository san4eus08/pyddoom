# константы настроек
import math

WIDTH = 800
HEIGHT = 600

ANGLE = 0.05

FPS = 15

TILE = 53.3
FOV = 0.8
NRAYS = 80
DELTA_ANGLE = FOV/NRAYS
MAX_DEPTH = 600

DIST = NRAYS / (2 * math.tan(FOV/2))
PROJ_COEFF = 3.5 * DIST * TILE
SCALE = WIDTH // NRAYS

# настройки игрока
player_pos = (WIDTH//2, HEIGHT//2)
player_angle = 0
player_speed = 3

# цвета(чтобы заного каждый раз не печатать)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (125, 125, 125)

# карта
text_map = [
    'XXXXXXXXXXXXXXX',
    'X.............X',
    'X.............X',
    'X.............X',
    'X.............X',
    'X.............X',
    'X.............X',
    'X.............X',
    'X.............X',
    'X.............X',
    'XXXXXXXXXXXXXXX'
]
world_map = set()
for i, row in enumerate(text_map):
    for j, char in enumerate(row):
        if char == "X":
            world_map.add((j * TILE, i * TILE))
