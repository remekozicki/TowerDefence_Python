import pygame
import math
from GameEngine.Button import Button


from pygame.sprite import OrderedUpdates
class Menu:
    def __init__(self, screen):
        self.screen = screen
        # self.show_main_screen()
        self.visible = True
        self.width = 400
        self.height = 500
        self.add_buttons()


    def add_buttons(self):
        button_width = 200
        button_height = 70
        self.buttons = []
        play_button = Button((self.screen.get_width() - button_width)//2, (self.screen.get_height() - self.height) //2 + 50, button_width, button_height, 'PLAY', lambda: self.hide_menu())
        self.buttons.append(play_button)

    def draw(self):

        pygame.draw.rect(self.screen, (0.1, 0.2, 100), pygame.Rect((self.screen.get_width()-self.width)//2, (self.screen.get_height()-self.height)//2, self.width, self.height))
        for button in self.buttons:
            button.process(self.screen)

    def hide_menu(self):
        self.visible = False
