#  This module will contain all classes and funcitons for drawing on the window.
import pygame
from load_sprits import sprite_loader
from players import player, npc
from buttons import all_buttons
from zones import zones_class
import itertools


# DrawGame will handle all drawing to the screen.
class BlitGame:
    def __init__(self):
        infos = pygame.display.Info()
        self.screen_size = (infos.current_w, infos.current_h)

        self.font_for_info = pygame.font.SysFont('comicsand', 30, True)

        self.fullscreen = True
        self.playingfield_resized = pygame.transform.scale(sprite_loader.playing_field,
                                                           (self.screen_size[0], self.screen_size[1]))
        self.counter = itertools.cycle([0, 1, 2, 3, 4])  # creating a recyclable counter for printing indexes.
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption('Duel Masters')

    def blit_hand(self):
        for card in player.cards_in_hand:
            if not card.is_picked_up:
                card.blit_card(player.mouse_pos(), self.window)

        if player.picked_up_card:
            player.picked_up_card.blit_card(player.mouse_pos(), self.window)

        for card in npc.cards_in_hand:
            card.blit_card((), self.window)

    def blit_shields(self):
        for card in player.shields:
            card_back = pygame.transform.scale(sprite_loader.card_back,  # the card size is scaling with screen res.
                                               (int(self.screen_size[0]*0.052), int(self.screen_size[1]*0.13)))
            self.window.blit(card_back, zones_class.shieldzone.positions_player[card.pos_index])

        for card in npc.shields:
            card_back = pygame.transform.scale(sprite_loader.card_back,
                                               (int(self.screen_size[0]*0.052), int(self.screen_size[1]*0.13)))
            self.window.blit(card_back, zones_class.shieldzone.positions_npc[card.pos_index])

    def blit_mana_zone(self):
        pygame.draw.rect(self.window, (0, 0, 0), zones_class.manazone.rect)
        for card in player.cards_in_mana_zone:
            card.blit_card((0, 0), self.window)

        for card in npc.cards_in_mana_zone:
            card.blit_card((0, 0), self.window)

    def blit_battle_zone(self):
        pygame.draw.rect(self.window, (255, 0, 0), zones_class.battlezone.rect)
        for card in player.cards_in_battle_zone:
            card.blit_card(player.mouse_pos(), self.window)

        for card in npc.cards_in_battle_zone:
            card.blit_card((0, 0), self.window)

    def blit_graveyard(self):
        pass

    def blit_info(self):
        text = self.font_for_info.render(player.current_phase, 1, (0, 0, 0))
        self.window.blit(text, (self.screen_size[0]*0.88, self.screen_size[1]*0.87))

        text = self.font_for_info.render(npc.current_phase, 1, (0, 0, 0))
        self.window.blit(text, (self.screen_size[0]*0.2, self.screen_size[1]*0.1))

    def blit_buttons(self):
        for key in all_buttons:
            if key == "attack":
                if player.current_phase == "attack":
                    all_buttons[key].blit(self.window)
            else:
                all_buttons[key].blit(self.window)

    def blit_window(self):
        self.window.blit(self.playingfield_resized, (0, 0))  # takes an image and an position.
        self.blit_buttons()
        self.blit_shields()
        self.blit_mana_zone()
        self.blit_battle_zone()
        self.blit_hand()
        self.blit_info()
        pygame.display.update()


blit_game = BlitGame()
