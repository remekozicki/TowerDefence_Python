import pygame

class Button:

    def __init__(self, x, y, width, height, text, on_click_functon=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onClickFuncton = on_click_functon
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont('Arial', 40)
        self.buttonSurf = font.render(text, True, (20, 20, 20))
