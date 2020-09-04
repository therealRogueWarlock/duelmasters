#  This module will contain a class for the players and opponent.
import random
import pygame
from zones import zones_class
import itertools
from cards_lib import card_classes
from utils import percent_of_screen_width, percent_of_screen_height

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

        # creates a list of card objects with the "ACard" class.
        self.deck_list = [card_classes.ACard(name) for name in self.saved_deck]
        self.cards_in_hand = []
        self.cards_in_shields = []
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
        self.turn_counter = 0

        # attributes for mana management.
        self.available_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0, "Water": 0}
        self.floating_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0, "Water": 0}
        # keeps track of how much mana is floating for a player.
        # when a card in the manazone is clicked "tapped" the card charges mana for the player to use.

        self.battlezone = zones_class.battlezone
        self.battlezone_position = (percent_of_screen_width(6.25), percent_of_screen_height(46))
        self.battlezone_slots = []

        self.positions_in_manazone = zones_class.manazone.positions_player

        self.graveyard = zones_class.graveyard
        self.graveyard_position = (percent_of_screen_width(65), percent_of_screen_height(80))
        self.graveyard.set_position(self.graveyard_position)

        self.shield_slots = []
        self.shield_zone = zones_class.shieldzone
        self.shield_zone_position = (percent_of_screen_width(6.25), percent_of_screen_height(60.2))

        self.hand_pos_x = (0.465, 0.29)
        self.hand_pos_y = 0.91

        self.target_card = None  # Target an enemy card
        self.selected_card = None  # select own card.

        # bool for if player charged mana this turn.
        self.if_charged_mana = False

        self.enemy = None

        # defining fonts for player info.
        self.font_for_phase_info = pygame.font.SysFont('comicsand', 30, True)

        self.font_for_info = pygame.font.SysFont('comicsand', 30, True)

        self.font_for_mana_info = pygame.font.SysFont('comicsand', 30, True)

    def create_zones(self):
        self.shield_slots = self.shield_zone.create_slots(self.shield_zone_position)
        self.battlezone_slots = self.battlezone.create_slots(self.battlezone_position)

    def shuffle_deck(self):
        return random.shuffle(self.deck_list)

    def draw_hand(self):
        for _ in range(5):  # Draw five cards.
            try:
                self.draw_a_card()
            except IndexError:
                print('Deck is out of cards.')

    def draw_shields(self):
        for i in range(5):  # Draw five cards.
            try:
                first_card = self.deck_list[0]  # the first card in the deck
                self.cards_in_shields.append(first_card)  # adding the first card of the deck to shields.
                first_card.pos_index = len(self.cards_in_shields) - 1  # -1 cause we count after we appended the card.
                first_card.set_position_to(self.shield_slots[first_card.pos_index])
                first_card.is_in_shield_zone()  # the card now know its zone.
                self.deck_list.remove(first_card)  # removing the first card from the deck.
            except IndexError:
                print('Deck is out of cards.')

    def put_shield_in_hand(self, shield_card):
        if shield_card.triggers:
            # if shield trigger, the it can be played for free imidetly
            pass

        else:
            self.cards_in_hand.append(shield_card)  # adding shield card of hand.
            shield_card.pos_index = len(self.cards_in_hand) - 1  # -1 cause we count after we appended the card.
            self.cards_in_shields.remove(shield_card)
            shield_card.is_in_hand()
            self.position_cards_in_hand()

    def draw_a_card(self):
        try:
            card_drawn = self.deck_list[0]
            self.cards_in_hand.append(card_drawn)  # adding the first card of the deck to hand.
            # the card now has an index of what position the card is in.
            card_drawn.pos_index = len(self.cards_in_hand) - 1  # -1 cause we count after we appended the card.
            card_drawn.is_in_hand()
            self.deck_list.remove(card_drawn)  # removing the first card from the deck.
            self.position_cards_in_hand()

        except IndexError:
            print('Deck is out of cards.')

    def position_cards_in_hand(self):
        for i, card in zip(itertools.count(), self.cards_in_hand):
            card.pos_index = i

        hand_size = len(self.cards_in_hand)
        screen_width = screen_size[0]
        screen_height = screen_size[1]
        positions_in_hand = []
        # as long as hand size is less then 7 there will be no card overlapping
        if hand_size < 7:
            positions_in_hand = [
                ((int(screen_size[0] * (self.hand_pos_x[0] - (0.025 * hand_size)) + x * int(screen_size[0] * 0.051))),
                 int(screen_size[1] * self.hand_pos_y)) for x in range(hand_size)]

        # creats a list of positions according to hand img_width and hand size.
        else:
            max_hand_width = screen_width * 0.3125  # the width of the hand is max 31 % of the screen.

            hand_spot_size = int(max_hand_width / hand_size)  # the size of the spots are determent by hand size-

            # overlap is how much the cards overlap.
            overlap = percent_of_screen_width(5.3) - hand_spot_size

            for card in self.cards_in_hand:  # reduce the card box my overlap size.

                card.width = percent_of_screen_width(5.3) - overlap

                if card == self.cards_in_hand[-1]:  # if its the last card in hand, no need to make the box smaller.
                    card.width = percent_of_screen_width(5.3)

            for x in range(hand_size):  # create a list the size of the hand.

                # the position of the hand on x-axes
                move_hand_left = int(screen_width * self.hand_pos_x[1] + (hand_spot_size / 3))

                card_pos_x = move_hand_left + hand_spot_size * x

                positions_in_hand.append((card_pos_x, int(screen_height * self.hand_pos_y)))

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
            self.picked_up_card.set_position_to(self.positions_in_manazone[self.picked_up_card.pos_index])
            self.cards_in_mana_zone.append(self.picked_up_card)
            self.cards_in_hand.remove(self.picked_up_card)
            self.picked_up_card = None
            self.if_charged_mana = True
        except Exception as error:
            print(error)
            print('No card picked')

    def put_card_in_graveyard(self, card):
        print(f"{self.name} put's {card.name} into the graveyard")

        card.location.remove(card)

        card.pos_index = len(self.cards_in_graveyard)

        card.set_position_to(self.graveyard_position)  # needs to be pos of graveyard

        self.cards_in_graveyard.append(card)

    def untap_cards(self):
        for card in (self.cards_in_battle_zone + self.cards_in_mana_zone):
            card.is_tapped = False
            card.is_used = False
            card.summoning_sickness = False
            card.width = percent_of_screen_width(5.3)
            card.height = percent_of_screen_height(3.5)
        self.if_charged_mana = False

    def play_card(self):
        print(f"{self.name} tries to play's {self.picked_up_card.name}")

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
                self.floating_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0}  # really needs a FIX!
        else:
            print("mana requirements not met.")

    def setup(self):
        for card in self.deck_list:
            card.owner = self

        self.create_zones()
        self.shuffle_deck()
        self.draw_shields()
        self.draw_hand()

    def shuffle_back_cards(self):
        self.deck_list = [card_classes.ACard(name) for name in self.saved_deck]
        self.cards_in_hand = []
        self.cards_in_shields = []
        self.cards_in_mana_zone = []
        self.cards_in_graveyard = []
        self.cards_in_battle_zone = []

    def get_interactive_cards(self):
        self.interactive_cards = (
                self.cards_in_hand + self.cards_in_mana_zone
                + self.cards_in_battle_zone + self.cards_in_shields)
        interactive_cards = self.interactive_cards
        return interactive_cards

    def next_phase(self):
        # will automatically go to next phase

        self.current_phase = next(self.turn_phases)  # cycles over turn phases.

        if self.current_phase == "untap":
            self.untap_phase()  # calling the untap phase.

        if self.current_phase == "draw":
            if not self.turn_counter == 0:  # if not starting draw card.
                self.draw_phase()
            else:
                self.next_phase()

        if self.current_phase == "charge":
            self.charge_phase()

        if self.current_phase == "main":
            self.main_phase()

        if self.current_phase == "attack":
            # when going from main step to attack. remove all floating mana, set it to 0.
            self.floating_mana = {"Darkness": 0, "Light": 0, "Fire": 0, "Nature": 0}
            self.attack_phase()

        if self.current_phase is None:
            self.turn_counter += 1

    def untap_phase(self):
        # has to check for effects at this step.
        self.untap_cards()
        # if no interatcion with effects, just call next_phase
        self.next_phase()

    def draw_phase(self):
        self.draw_a_card()
        self.next_phase()

    def charge_phase(self):
        if len(self.cards_in_hand) == 0:  # if no cards in hand, just go to next phase.
            self.next_phase()

    def main_phase(self):
        # can play cards with mana.
        # might be able to auto pass if player cant play a card.
        pass

    def attack_phase(self):
        if self.can_attack():
            pass  # player can now choose to attack, or go to next phase.
        else:
            self.next_phase()

    def end_phase(self):
        # check if any of players cards has an endstep trigger.
        for card in self.cards_in_battle_zone + self.cards_in_mana_zone:
            pass

    def manage_cards_in_hand(self):
        if self.picked_up_card:  # moving around cards in hand.
            for card in self.cards_in_hand:
                if not card == self.picked_up_card:
                    if card.mouse_is_over(self.mouse_pos()):
                        self.position_cards_in_hand()
                        switch_index = card.pos_index  # store card index.

                        self.cards_in_hand.remove(card)
                        self.cards_in_hand.insert(self.picked_up_card.pos_index, card)

                        self.cards_in_hand.remove(self.picked_up_card)
                        self.cards_in_hand.insert(switch_index, self.picked_up_card)

                        self.position_cards_in_hand()

    def info(self):
        return f'picked card: {self.picked_up_card}'

    def player_info(self):
        return f'player decklist ({len(self.deck_list)}): {[card.name for card in self.deck_list]}\n' \
               f'player hand ({len(self.cards_in_hand)}): {[card.name for card in self.cards_in_hand]}\n' \
               f'player shields ({len(self.cards_in_shields)}): {[card.name for card in self.cards_in_shields]}\n' \
               f'player manazone ({len(self.cards_in_mana_zone)}): {[card.name for card in self.cards_in_mana_zone]}\n' \
               f'available mana {self.available_mana}' \
               f'saved deck {self.saved_deck}\n' \
               f'mana {self.available_mana}\n' \
               f'float mana {self.floating_mana}\n'

    def can_attack(self):  # will check if any card in the battlezone can attack.
        for card in self.cards_in_battle_zone:
            if not card.summoning_sickness:
                if not card.is_used:
                    if not card.is_tapped:
                        return True
        return False


class NpcOpponent(Player):
    def __init__(self):
        super().__init__()

        self.saved_deck = ['DeadlyFighterBraidClaw', 'ArmoredWalkerUrherion', 'ArmoredWalkerUrherion', 'ArtisanPicora',
                           'ArtisanPicora', 'BolshackDragon', 'BrawlerZyler', 'BrawlerZyler', 'BrawlerZyler',
                           'DeadlyFighterBraidClaw', 'FatalAttackerHorvath', 'FatalAttackerHorvath',
                           'FatalAttackerHorvath', 'FatalAttackerHorvath', 'FireSweeperBurningHellion',
                           'FireSweeperBurningHellion', 'FireSweeperBurningHellion', 'ImmortalBaronVorg',
                           'ImmortalBaronVorg', 'ImmortalBaronVorg', 'ImmortalBaronVorg']

        self.deck_list = [card_classes.ACard(name) for name in self.saved_deck]

        self.battlezone_position = (percent_of_screen_width(6.25), percent_of_screen_height(30))

        self.positions_in_manazone = zones_class.manazone.positions_npc

        self.graveyard_position = (percent_of_screen_width(30), percent_of_screen_height(20))

        self.shield_zone_position = (percent_of_screen_width(6.25), percent_of_screen_height(20))

        self.hand_pos_x = (0.665, 0.29)
        self.hand_pos_y = 0.05

        self.turn_counter = 1

    # hardcoded AI
    def next_phase(self):  # npc will have its onew next_phase methode. all the actions has to be automated.

        self.current_phase = next(self.turn_phases)  # cycles over turn phases.
        if self.current_phase == "untap":
            self.untap_cards()

        if self.current_phase == "draw":
            if not self.turn_counter == 0:  # if not starting draw card.
                self.draw_a_card()

        if self.current_phase == "charge":
            # TODO need more logic
            if len(self.cards_in_hand) > 2:
                if len(self.cards_in_mana_zone) < 6:
                    max_mana_cost = 0
                    for card in npc.cards_in_hand:
                        if card.mana_cost > max_mana_cost:
                            max_mana_cost = card.mana_cost
                            self.picked_up_card = card
                    self.put_card_in_mana_zone()

        if self.current_phase == "main":
            available_mana = self.available_mana['Fire']  # plays with mono color.
            print(f'npc mana {available_mana}')

            # sorting cards in hand by mana cost in a new list.
            sorted_by_mana_cost = sorted(self.cards_in_hand, key=lambda card: card.mana_cost, reverse=True)

            for card in sorted_by_mana_cost:
                if card.mana_cost <= available_mana:
                    self.picked_up_card = card

                    for card in self.cards_in_mana_zone:
                        if not card.is_tapped:
                            print(f'npc tap {card.name}')
                            card.is_clicked()

                        if self.floating_mana['Fire'] == self.picked_up_card.mana_cost:
                            break
                    available_mana -= self.picked_up_card.mana_cost
                    self.play_card()

        if self.current_phase == "attack":
            pair_up_cards = []  # will pair up the cards in tuples.
            cards_that_can_attack = []
            cards_for_target = []

            # first find all cards that can attack.
            for card in self.cards_in_battle_zone:
                if not card.summoning_sickness:
                    if not card.is_used:
                        if not card.is_tapped:
                            cards_that_can_attack.append(card)

            print(f'{self.name}, can attack with {[card.name for card in cards_that_can_attack]}')
            # then find all available targets.
            for card in self.enemy.cards_in_battle_zone:
                print('player battlezone ', card.name)
                if not card.is_tapped:
                    cards_for_target.append(card)

            # find the best target for available target
            for card in cards_that_can_attack:  # check every card
                for target in cards_for_target:  # check card vs a target.
                    if card.power > target.power:  # if the card has higher power than the target its a good fight.
                        pair_up_cards.append((card, target))
                        print('good target')
                    elif card.power == target.power:
                        print('trade')

            # if npc has more shields than player attackers.
            for card in cards_that_can_attack:
                if len(self.cards_in_shields) > len(self.enemy.cards_in_battle_zone):
                    # attack a shield
                    if not len(self.enemy.cards_in_shields) == 0:
                        shield_card = random.choice(self.enemy.cards_in_shields)
                        print(card.name, 'attack shield', shield_card.pos_index)
                        card.fight(shield_card)
                    else:
                        print(f'{self.name} wins!')

            for pair in pair_up_cards:
                print(pair[0].name, pair[1].name)

        if self.current_phase is None:
            self.turn_counter += 1


player = Player()
player.name = "sander"

npc = NpcOpponent()
npc.name = "npc"

player.enemy = npc
npc.enemy = player

npc.setup()
player.setup()

