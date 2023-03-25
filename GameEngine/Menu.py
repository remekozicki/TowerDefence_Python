import pygame
import math
from pygame.sprite import OrderedUpdates
class Menu:
    def __init__(self):

        self.components = OrderedUpdates()
        self.show_main_screen()
        self.visible = True

    def add_button(self, text):
        button = MenuButton()