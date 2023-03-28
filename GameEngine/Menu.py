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
        play_button = Button((self.screen.get_width() - button_width) // 2,
                             (self.screen.get_height() - self.height) // 2 + 50, button_width, button_height, 'PLAY', self.hide_menu)
        levels_button = Button((self.screen.get_width() - button_width) // 2,
                             (self.screen.get_height() - self.height) // 2 + 130, button_width, button_height, 'LEVELS')
        settings_button = Button((self.screen.get_width() - button_width) // 2,
                               (self.screen.get_height() - self.height) // 2 + 210, button_width, button_height,
                               'SETTINGS')
        quit_button = Button((self.screen.get_width() - button_width) // 2,
                             (self.screen.get_height() - self.height) // 2 + 290, button_width, button_height, 'QUIT',self.quit_game)
        self.buttons.append(play_button)
        self.buttons.append(levels_button)
        self.buttons.append(settings_button)
        self.buttons.append(quit_button)

    def draw(self):
        pygame.draw.rect(self.screen, (0.1, 0.2, 100), pygame.Rect((self.screen.get_width() - self.width) // 2,
                                                                   (self.screen.get_height() - self.height) // 2,
                                                                   self.width, self.height))
        for button in self.buttons:
            button.process(self.screen)

    def menu_clicked(self):
        for button in self.buttons:
            button.click()

    def hide_menu(self):
        self.visible = False

    def quit_game(self):
        raise SystemExit
