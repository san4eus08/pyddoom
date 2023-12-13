import pygame

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.position = self.x, self.y, self.width, self.height = x, y, width, height
        self.color = pygame.Color(color)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.position, 0)


    def redraw_window(self):

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)