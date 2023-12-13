import pygame

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.position = self.x, self.y, self.width, self.height = x, y, width, height
        self.color = pygame.Color(color)
        self.text = pygame.font.Font(None, 30).render(text, True, (100, 255, 100))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.position, 1)
        screen.blit(self.text, (self.x - self.text.get_width() + self.width,
                                self.y - self.text.get_height() + self.height))

    def redraw_window(self):
        pass


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    button = Button(width // 2 - 50, height // 2 - 25, 100, 50, (0, 0, 0), 'Button')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        button.draw(screen)
        pygame.display.flip()