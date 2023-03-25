import pygame
import random


class Game:
    # contains basic controls and game loop

    def __init__(self, window):

        self.window = window
        self.clock = pygame.time.Clock()

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

            self.window.clear()
