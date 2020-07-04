import pygame
from cards_lib.card_dictionary import card_dict
from utils import percent_of_screen_width, percent_of_screen_height


# might create a class to handle load of sprits.


class SpriteLoader:
    def __init__(self):
        self.cards_dict = card_dict
        self.playing_field = pygame.image.load("Sprits/playingfield.png")

        self.card_back_raw = pygame.image.load("Sprits/pic43176.jpg")

        self.card_back = pygame.transform.scale(self.card_back_raw,
                                                (percent_of_screen_width(5.2), percent_of_screen_height(13)))

    def load_cards_sprits(self):  # Utilizing the card dictionary.
        for civilization in self.cards_dict.keys():
            for card_name in self.cards_dict[civilization].keys():
                card_dict[civilization][card_name]['img'] = pygame.image.load(f"cards_lib/DM_01_base_set/"
                                                                              f"{civilization}/{card_name}.jpg")


sprite_loader = SpriteLoader()

sprite_loader.load_cards_sprits()

