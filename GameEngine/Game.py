import pygame


class Game:
    # contains basic controls and game loop

    def __int__(self, window):
        # self.running = None
        self.window = window
        self.clock = pygame.time.Clock()
        # sprites (all moving objects which will be added later)
        # self.load_level('path')
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
