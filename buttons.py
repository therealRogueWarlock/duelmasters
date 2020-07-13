#  This module will contain a class for buttons and all the buttens used.
import pygame
from load_sprits import sprite_loader
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)


class button:
    def __init__(self, color, x, y, width, height, text='', img=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.img = img

    def blit(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        if self.img:
            img = pygame.transform.scale(self.img, (self.width, self.height))
            win.blit(img, (self.x, self.y))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', 60)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (self.x + round(self.width / 2 - text.get_width() / 2),
                                (self.y + round(self.height / 2 - text.get_height() / 2))))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


all_buttons = {"next_button": button((0, 96, 205), int(screen_size[0]*0.85), int(screen_size[1]*0.9),
                                     int(screen_size[0]*0.1), int(screen_size[1]*0.04), 'next'),
               "deck_button": button((0, 96, 205), int(screen_size[0]*0.65), int(screen_size[1]*0.7),
                                     int(screen_size[0]*0.053), int(screen_size[1]*0.127),
                                     'deck', img=sprite_loader.card_back),
               "attack": button((0, 96, 205), int(screen_size[0]*0.85), int(screen_size[1]*0.8),
                                     int(screen_size[0]*0.1), int(screen_size[1]*0.04), 'attack')}
