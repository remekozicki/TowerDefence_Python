import pygame
import random
from GameEngine.Menu import Menu

class Game:
    # contains basic controls and game loop

    def __init__(self, window):

        self.window = window
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.window.screen)

    def run(self):
        # main game loop

        self.running = True

        while self.running:

            delta = self.clock.tick(60) / 1000.0

            # quit events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.menu.visible:
                        self.menu.visible = True

            if(self.menu.visible):
                self.menu.draw()

            self.window.clear()
