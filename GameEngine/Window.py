import pygame


class Window:

    def __init__(self, width, height):

        self.dimensions = (width, height)
        self.screen = pygame.display.set_mode(self.dimensions)
        self.set_background(0, 0, 0)

    def set_background(self, r, g, b):
        self.background = pygame.Surface(self.dimensions)
        self.background.fill(pygame.Color(r, g, b))
        pygame.display.update()
        self.background = self.background.convert()

    def set_title(self, title):
        pygame.display.set_caption(title)


    def clear(self):
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))


