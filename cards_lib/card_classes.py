#  Creating a class for the cards dictionary.
from cards_lib.card_dictionary import card_dict
import pygame


infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)


# CardsDict will handle all data about the cards.
class CardsDict:
    def __init__(self):
        self.cards_dict = card_dict

    def info_card_by_name(self, name):
        for civilization in self.cards_dict.keys():
            for card_name in self.cards_dict[civilization].keys():
                if card_name == name:
                    return self.cards_dict[civilization][card_name]

    def civilization_by_name(self, name):
        for civilization in self.cards_dict.keys():
            for card_name in self.cards_dict[civilization].keys():
                if card_name == name:
                    return civilization


cards_dict_class = CardsDict()


class ACard:
    def __init__(self, name):
        # card info
        self.name = name
        self.civilization = cards_dict_class.civilization_by_name(name)
        self.card_type = card_dict[self.civilization][self.name]['Card Type']
        self.card_text = card_dict[self.civilization][self.name]['Card Text']
        self.mana_cost = card_dict[self.civilization][self.name]["Mana Cost"]
        self.power = card_dict[self.civilization][self.name]["Power"]
        self.race = card_dict[self.civilization][self.name]["Race"]

        # card properties.
        self.img = card_dict[self.civilization][self.name]["img"]
        self.info_img = pygame.transform.scale(self.img, (int(screen_size[0] * 0.159), int(screen_size[1] * 0.381)))

        self.pos_xy = (0, 0)
        self.pos_index = 0

        # card size
        self.width = int(screen_size[0] * 0.053)  # 100
        self.height = int(screen_size[1] * 0.127)   # 138

        # if the card i clicked by the mouse and can be picked up.
        self.is_picked_up = False

        # when the mouse is hovering over the card will show info.
        self.hover_over = False

        # if the card is used, it cant be used before next turn. (for attacking or for floating mana)
        self.is_used = False

        # blitting the card at a 90 angle if tapped.
        self.is_tapped = False

        # using bools for logic.
        self.in_graveyard = False
        self.in_battle_zone = False
        self.in_hand = False
        self.in_mana_zone = False
        self.in_shield_zone = False

        self.is_clicked_bool = False

        # check how owns the card.
        self.owner = None

        self.summoning_sickness = True

    # Card abilities/card triggers.
    def blocker(self):
        # a card with blocker can block an attack.
        pass

    def double_breaker(self):
        # when this card attacks a player the player will lose two shields if possible.
        pass

    def destroy(self):
        # check if card has an ability triggered on death.

        # calls the owner to put the card in the graveyard.
        self.owner.put_card_in_graveyard(self)
        self.is_in_graveyard()

    def fight(self, card):
        print(f'{self.name}, power {self.power} fights {card.name},  power {card.power}')

        if self.power > card.power:
            print(f'{self.name} wins')
            card.destroy()
        elif self.power == card.power:
            print(f'both die')
            self.destroy()
            card.destroy()
        else:
            print(f'{card.name} wins')
            self.destroy()

    def set_all_zones_to_false(self):
        self.in_graveyard = False
        self.in_battle_zone = False
        self.in_hand = False
        self.in_mana_zone = False
        self.in_shield_zone = False

    def is_in_mana_zone(self):
        print("card is in mana zone")
        self.set_all_zones_to_false()
        # makes the image smaller, will fit better in manazone
        self.img = pygame.transform.chop(self.img, (0, 45, 0, 215))
        self.width = int(screen_size[0] * 0.053)  # 100
        self.height = int(screen_size[1] * 0.035)  # 37
        self.in_mana_zone = True

    def is_in_battle_zone(self):
        self.set_all_zones_to_false()
        self.width = int(screen_size[0] * 0.053)  # 100
        self.height = int(screen_size[1] * 0.127)  # 138
        self.in_battle_zone = True

    def is_in_graveyard(self):
        self.set_all_zones_to_false()

    def set_position_to(self, new_pos):
        if self.is_picked_up:  # centering the card on the mouse.
            self.pos_xy = new_pos[0] - (self.width / 2), new_pos[1] - (self.height / 2)
            return self.pos_xy

        self.pos_xy = new_pos

        return self.pos_xy

    # create a function to blit it self.
    def blit_card(self, player_mouse_pos, window):
        # getting the img to blit, and resizing it.
        card_img = pygame.transform.scale(self.img, (self.width, self.height))

        if self.in_mana_zone:
            card_img = pygame.transform.flip(card_img, False, True)

        if self.is_tapped:
            # rotating the card 90 degrees if the card is tapped.
            card_img = pygame.transform.rotozoom(card_img, -90, 1)

        # if the card is clicked it will be highlighted.
        if self.is_clicked_bool:
            if not self.in_mana_zone:
                pygame.draw.rect(window, (250, 0, 0),
                                 (self.pos_xy[0] - 5, self.pos_xy[1] - 5, self.width + 10, self.height + 10))
                window.blit(self.info_img, (int(screen_size[0] * 0.825), int(screen_size[1] * 0.363)))

        if self.is_picked_up:
            # if that card is picked up, the card will get mouse pos.
            window.blit(card_img, self.set_position_to(player_mouse_pos))

        if self.hover_over:
            window.blit(self.info_img, (int(screen_size[0] * 0.625), int(screen_size[1] * 0.363)))

        window.blit(card_img, self.pos_xy)

    # functions for logic.
    def mouse_is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.pos_xy[0] < pos[0] < self.pos_xy[0] + self.width:
            if self.pos_xy[1] < pos[1] < self.pos_xy[1] + self.height:
                self.hover_over = True
                return True
        self.hover_over = False
        return False

    def is_clicked(self):
        if self.in_hand:
            self.is_picked_up = True
        if self.in_mana_zone:
            if not self.is_tapped:
                self.is_tapped = True
            else:
                self.is_tapped = False

    def is_double_clicked(self):
        if not self.is_clicked_bool:
            self.is_clicked_bool = True
            self.is_tapped = True
        else:
            self.is_clicked_bool = False
            self.is_tapped = False

