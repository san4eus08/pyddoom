# константы настроек
import math

WIDTH = 1500
HEIGHT = 1000

ANGLE = 0.05

FPS = 60

TILE = 100
FOV = math.pi / 3
NRAYS = 300
DELTA_ANGLE = FOV/NRAYS
MAX_DEPTH = 1200

DIST = NRAYS / (2 * math.tan(FOV/2))
PROJ_COEFF = 4 * DIST * TILE
SCALE = WIDTH // NRAYS

# наконец-то я добавил это
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
HALF_FOV = FOV / 2

# текстуры
TEXTURE_W, TEXTURE_H = WIDTH, WIDTH
TEXTURE_SCALE = WIDTH // TILE

# спрайты(вкусно)
DOUBLE_PI = math.pi * 2
CENTER_RAY = NRAYS // 2 - 1
FAKE_RAYS = 100

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
    '111111111111111',
    '1.............1',
    '1.............1',
    '1...22........1',
    '1...22........1',
    '1.............1',
    '1.............1',
    '1.............1',
    '1.............1',
    '1.............1',
    '111111111111111'
]

world_map = {}
for i, row in enumerate(text_map):
    for j, char in enumerate(row):
        if char == "1":
            world_map[(j * TILE, i * TILE)] = '1'
        elif char == "2":
            world_map[(j * TILE, i * TILE)] = '2'
