import pygame
from cards_lib.card_dictionary import card_dict

# might create a class to handle load of sprits.


class SpriteLoader:
    def __init__(self):
        self.cards_dict = card_dict
        self.playing_field = pygame.image.load("Sprits/playingfield.png")
        self.card_back = pygame.image.load("Sprits/pic43176.jpg")

    def load_cards_sprits(self):  # Utilizing the card dictionary.
        for civilization in self.cards_dict.keys():
            for card_name in self.cards_dict[civilization].keys():
                card_dict[civilization][card_name]['img'] = pygame.image.load(f"cards_lib/DM_01_base_set/"
                                                                              f"{civilization}/{card_name}.jpg")


sprite_loader = SpriteLoader()

sprite_loader.load_cards_sprits()

