#  This module will contain a class for the players and opponent.
import random
import pygame
from zones import zones_class
import itertools
from cards_lib import card_classes

infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)


class Player:
    def __init__(self):

        self.name = "noName"

        self.saved_deck = ['WrithingBoneGhoul', 'WrithingBoneGhoul', 'WrithingBoneGhoul',
                           'WrithingBoneGhoul', 'DeathSmoke', 'DeathSmoke', 'MieleVizierofLightning',
                           'MieleVizierofLightning', 'MieleVizierofLightning', 'LaUraGigaSkyGuardian',
                           'LaUraGigaSkyGuardian', 'ToelVizierofHope', 'SzubsKinTwilightGuardian',
                           'SenatineJadeTree', 'RubyGrass', 'CreepingPlague', 'BoneSpider',
                           'SuperExplosiveVolcanodon', 'Stonesaur', 'ScarletSkyterror',
                           'RothusTheTraveler', 'SteelSmasher', 'GoldenWingStriker', 'BronzeArmTribe']

        # saving the deck two places, will help when resetting.

        self.turn_counter = 0

        # creates a list of card objects with the "ACard" class.
        self.deck_list = [card_classes.ACard(name) for name in self.saved_deck]
        self.cards_in_hand = []
        self.shields = []
        self.cards_in_mana_zone = []
        self.cards_in_graveyard = []
        self.cards_in_battle_zone = []

        self.interactive_cards = []

        # player input
        self.mouse_pos = pygame.mouse.get_pos  # mouse

        # if player has a card picked up.
        self.picked_up_card = None

        self.in_game = True

        # attributes for a round and the phases
        self.turn_phases = itertools.cycle(["untap", "draw", "charge", "main", "attack", "end", None])
        self.current_phase = None

        # attributes for mana management.
        self.available_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0, "Water": 0}
        self.floating_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0, "Water": 0}
        # keeps track of how much mana is floating for a player.
        # when a card in the manazone is clicked "tapped" the card charges mana for the player to use.

        self.positions_in_battlezone = zones_class.battlezone.positions_player

        self.target_card = None  # Target an enemy card
        self.selected_card = None  # select own card.

        # check if player chaged this turn.
        self.if_charged_mana = False

    def shuffle_deck(self):
        return random.shuffle(self.deck_list)

    def draw_hand(self):
        for i in range(5):  # Draw five cards.
            try:
                self.draw_a_card()
            except IndexError:
                print('Deck is out of cards.')

    def draw_shields(self):
        for i in range(5):  # Draw five cards.
            try:
                self.shields.append(self.deck_list[0])  # adding the first card of the deck to shields.
                self.deck_list[0].pos_index = len(self.shields) - 1  # -1 cause we count after we appended the card.
                self.deck_list[0].in_shield_zone = True  # the card now know its zone.
                self.deck_list.remove(self.deck_list[0])  # removing the first card from the deck.
            except IndexError:
                print('Deck is out of cards.')

    def draw_a_card(self):
        try:
            card_drawn = self.deck_list[0]
            self.cards_in_hand.append(card_drawn)  # adding the first card of the deck to hand.
            # the card now has an index of what position the card is in.
            card_drawn.pos_index = len(self.cards_in_hand) - 1  # -1 cause we count after we appended the card.
            card_drawn.in_hand = True  # the card now know its location.
            self.deck_list.remove(card_drawn)  # removing the first card from the deck.
            self.position_cards_in_hand()

        except IndexError:
            print('Deck is out of cards.')

    def position_cards_in_hand(self):
        positions_in_hand = [((int(screen_size[0] * 0.425) + x),
                              int(screen_size[1] * 0.83334)) for x in range(len(self.cards_in_hand))]

        for card in self.cards_in_hand:
            card.set_position_to(positions_in_hand[card.pos_index])

    def float_mana(self, card):
        # check if card is tapped or not.
        if card.is_tapped:
            self.floating_mana[card.civilization] += 1
        else:
            self.floating_mana[card.civilization] -= 1

    def put_card_in_mana_zone(self):
        try:
            print(f"put {self.picked_up_card.name} into mana zone")
            self.available_mana[self.picked_up_card.civilization] += 1
            self.picked_up_card.is_picked_up = False
            self.picked_up_card.is_in_mana_zone()
            self.picked_up_card.pos_index = len(self.cards_in_mana_zone)
            self.picked_up_card.set_position_to(zones_class.manazone.positions_player[self.picked_up_card.pos_index])
            self.cards_in_mana_zone.append(self.picked_up_card)
            self.cards_in_hand.remove(self.picked_up_card)
            self.picked_up_card = None
            self.if_charged_mana = True
        except Exception as error:
            print(error)
            print('No card picked')

    def put_card_in_graveyard(self, card):
        print(f"{self.name} put's {card.name} into the graveyard")
        card.is_clicked_bool = False

        card.pos_index = len(self.cards_in_graveyard)
        card.set_position_to((1000, 800))  # needs to be pos of graveyard
        self.cards_in_graveyard.append(card)

        card.is_in_graveyard()

    def play_card(self):
        # TODO should be able to auto tap mana, when playing a card.
        print(f"{self.name} play's {self.picked_up_card.name}")
        # first check if players floating mana meets the cards requirements.
        # check if the player has at least one mana of the right color.
        if self.floating_mana[self.picked_up_card.civilization] >= 1:
            total_floting_mana = 0
            for civilization in self.floating_mana:
                total_floting_mana += self.floating_mana[civilization]

            if total_floting_mana >= self.picked_up_card.mana_cost:
                self.picked_up_card.is_picked_up = False
                self.picked_up_card.is_in_battle_zone()
                self.picked_up_card.pos_index = len(self.cards_in_battle_zone)
                self.picked_up_card.set_position_to(self.positions_in_battlezone[self.picked_up_card.pos_index])
                self.cards_in_battle_zone.append(self.picked_up_card)
                self.cards_in_hand.remove(self.picked_up_card)
                self.picked_up_card = None
                # needs to only use mana consumed by the card, atm just reset floating mana after play.
                #self.floating_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0}  # really needs a FIX!
        else:
            print("mana requirements not met.")

    def setup(self):
        for card in self.deck_list:
            card.owner = self

        self.shuffle_deck()
        self.draw_shields()
        self.draw_hand()

    def shuffle_back_cards(self):
        self.deck_list = [card_classes.ACard(name) for name in self.saved_deck]
        self.cards_in_hand = []
        self.shields = []
        self.cards_in_mana_zone = []
        self.cards_in_graveyard = []
        self.cards_in_battle_zone = []

    def get_interactive_cards(self):
        self.interactive_cards = (self.cards_in_hand + self.cards_in_graveyard + self.cards_in_mana_zone + self.cards_in_battle_zone)
        interactive_cards = self.interactive_cards
        return interactive_cards

    def next_phase(self):
        self.current_phase = next(self.turn_phases)  # cycles over turn phases.
        print(self.name, self.current_phase)
        if self.current_phase == "untap":
            self.untap_cards()

        if self.current_phase == "draw":
            if not self.turn_counter == 0:  # if not starting draw card.
                self.draw_a_card()

    def untap_cards(self):
        for card in (self.cards_in_battle_zone + self.cards_in_mana_zone):
            card.is_tapped = False
        self.if_charged_mana = False

    def main(self):
        # can play cards with mana.
        pass

    def attack_step(self):
        pass

    def end_step(self):
        # check if any of players cards has an endstep trigger.
        for card in self.cards_in_battle_zone + self.cards_in_mana_zone:
            pass

    def info(self):
        return f'picked card: {self.picked_up_card}'

    def player_info(self):
        return f'player decklist ({len(self.deck_list)}): {[card.name for card in self.deck_list]}\n ' \
               f'player hand ({len(self.cards_in_hand)}): {[card.name for card in self.cards_in_hand]}\n ' \
               f'player shields ({len(self.shields)}): {[card.name for card in self.shields]}\n ' \
               f'player manazone ({len(self.cards_in_mana_zone)}): {[card.name for card in self.cards_in_mana_zone]}\n'\
               f'player active ({len(self.interactive_cards)}): {[card.name for card in self.interactive_cards]}\n' \
               f'saved deck {self.saved_deck}\n' \
               f'mana {self.available_mana}\n' \
               f'float mana {self.floating_mana}' \



class NpcOpponent(Player):
    def __init__(self):
        super().__init__()

        self.saved_deck = ['MieleVizierofLightning', 'MieleVizierofLightning', 'NightMasterShadowofDecay',
                           'MieleVizierofLightning', 'LaUraGigaSkyGuardian', 'LaUraGigaSkyGuardian', 'GhostTouch',
                           'Gigaberos', 'Gigagiele', 'SkeletonSoldiertheDefiled', 'WrithingBoneGhoul', 'WrithingBoneGhoul', 'WrithingBoneGhoul',
                           'WrithingBoneGhoul', 'DeathSmoke', 'DeathSmoke', 'MieleVizierofLightning',
                           'MieleVizierofLightning', 'MieleVizierofLightning', 'LaUraGigaSkyGuardian',
                           'LaUraGigaSkyGuardian', 'ToelVizierofHope', 'SzubsKinTwilightGuardian',
                           'SenatineJadeTree', 'RubyGrass', 'CreepingPlague', 'BoneSpider',
                           'SuperExplosiveVolcanodon', 'Stonesaur', 'ScarletSkyterror',
                           'RothusTheTraveler', 'SteelSmasher', 'GoldenWingStriker', 'BronzeArmTribe']

        self.deck_list = [card_classes.ACard(name) for name in self.saved_deck]

        self.positions_in_battlezone = zones_class.battlezone.positions_npc


player = Player()
player.name = "sander"
npc = NpcOpponent()
npc.name = "npc"

npc.setup()
player.setup()







