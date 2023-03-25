
import pygame
from GameEngine.Game import Game
from GameEngine.Window import Window

# Init pygame
pygame.init()

# Create a window
window = Window(1280, 768)
window.set_title("Tower Defence")
window.set_background(148, 0, 0)

# Create the game instance
game = Game(window)
game.run()

# Quit pygame
pygame.quit()
