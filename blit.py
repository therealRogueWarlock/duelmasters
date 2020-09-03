#  This module will contain all classes and funcitons for drawing on the window.
import pygame
from utils import percent_of_screen_width, percent_of_screen_height
from load_sprits import sprite_loader
from players import player, npc
from buttons import all_buttons
from zones import zones_class


# BlitGame will handle all drawing to the screen.
class BlitGame:
    def __init__(self):
        self.font_for_phase_info = pygame.font.SysFont('comicsand', 30, True)
        self.font_for_info = pygame.font.SysFont('comicsand', 30, True)
        self.font_for_mana_info = pygame.font.SysFont('comicsand', 30, True)

        infos = pygame.display.Info()
        self.screen_size = (infos.current_w, infos.current_h)

        self.font_for_info = pygame.font.SysFont('comicsand', 30, True)

        self.fullscreen = True
        self.playingfield_resized = \
            pygame.transform.scale(sprite_loader.playing_field,
                                   (percent_of_screen_width(100), percent_of_screen_height(100)))

        infos = pygame.display.Info()
        self.screen_size = (infos.current_w, infos.current_h)

        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption('Duel Masters')

    def blit_hand(self):
        for card in player.cards_in_hand:
            if not card.is_picked_up:
                card.blit_card(self.window)

        if player.picked_up_card:
            player.picked_up_card.blit_card(self.window)

        for card in npc.cards_in_hand:
            card.blit_card(self.window)

    def blit_shields(self):
        for card in player.cards_in_shields:
            card.blit_card(self.window)

        for card in npc.cards_in_shields:
            card.blit_card(self.window)

    def blit_mana_zone(self):
        pygame.draw.rect(self.window, (20, 20, 20), zones_class.manazone.rect)
        for card in player.cards_in_mana_zone:
            card.blit_card(self.window)

        for card in npc.cards_in_mana_zone:
            card.blit_card(self.window)

    def blit_battle_zone(self):
        pygame.draw.rect(self.window, (255, 0, 0), zones_class.battlezone.rect)
        for card in player.cards_in_battle_zone:
            card.blit_card(self.window)

        for card in npc.cards_in_battle_zone:
            card.blit_card(self.window)

    def blit_graveyard(self):
        for card in player.cards_in_graveyard:
            card.blit_card(self.window)

        for card in npc.cards_in_graveyard:
            card.blit_card(self.window)

    def blit_info(self):
        # blitting info for floating mana.
        index = 0
        for civilization in player.floating_mana:
            if player.floating_mana[civilization] > 0:
                self.window.blit(sprite_loader.civilization_ikons[civilization],
                                 (percent_of_screen_width(45 + index),
                                  percent_of_screen_height(87)))

                index += 2.5
                text = self.font_for_mana_info.render(str(player.floating_mana[civilization]), 1, (0, 0, 0))
                self.window.blit(text, (percent_of_screen_width(45 + index),
                                        percent_of_screen_height(87)))

                index += 2.5

        text = self.font_for_phase_info.render(player.current_phase, 1, (0, 0, 0))
        self.window.blit(text, (percent_of_screen_width(88), percent_of_screen_height(87)))

        text = self.font_for_info.render(npc.current_phase, 1, (0, 0, 0))
        self.window.blit(text, (percent_of_screen_width(88), percent_of_screen_height(20)))

    def blit_buttons(self):
        for key in all_buttons:
            if key == "attack":
                if player.current_phase == "attack":
                    all_buttons[key].blit(self.window)
            else:
                all_buttons[key].blit(self.window)

    def blit_window(self):
        self.window.blit(self.playingfield_resized, (0, 0))  # takes an image and a position.
        self.blit_buttons()
        self.blit_shields()
        self.blit_mana_zone()
        self.blit_battle_zone()
        self.blit_graveyard()
        self.blit_hand()
        self.blit_info()
        pygame.display.update()


blit_game = BlitGame()
