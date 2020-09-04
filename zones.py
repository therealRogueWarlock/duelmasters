# This module will contain classes for the zones. might not make sens to make.
import pygame
from utils import percent_of_screen_width, percent_of_screen_height


class Zones:
    def __init__(self):
        self.x_pos = percent_of_screen_width(6.25)  # the overall x-position of a zone on the screen.
        self.manazone = self.ManaZone(self.x_pos)
        self.shieldzone = self.ShieldZone()
        self.battlezone = self.Battlezone(self.x_pos)
        self.graveyard = self.Graveyard()

    class Battlezone:
        def __init__(self, x_pos):
            # Battle zone
            # creating positions for cards in players battlezone
            self.pos_xy = (x_pos * 5, percent_of_screen_height(46))

            self.height = percent_of_screen_height(12.5)

            self.width = percent_of_screen_width(31)

            self.rect = (self.pos_xy[0], self.pos_xy[1], self.width, self.height)

        def mouse_is_over(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates.
            if self.pos_xy[0] < pos[0] < self.pos_xy[0] + self.width:
                if self.pos_xy[1] < pos[1] < self.pos_xy[1] + self.height:
                    return True
            return False

        def create_slots(self, pos_xy):
            battlezone_slots = [(pos_xy[0] * x, pos_xy[1]) for x in range(5, 45)]
            return battlezone_slots

    class ManaZone:
        def __init__(self, x_pos):
            # Mana zone
            # creating postions for cards in players manazone
            self.pos_xy = percent_of_screen_width(31), percent_of_screen_height(74)

            self.height = percent_of_screen_height(12.5)

            self.width = percent_of_screen_width(31)

            self.rect = (self.pos_xy[0], self.pos_xy[1], self.width, self.height)

            self.player_y_pos = percent_of_screen_height(74)

            self.positions_player = self.create_positions(x_pos)

            # creating positions for cards in npc manazone
            self.npc_y_pos = percent_of_screen_height(5.2)
            self.positions_npc = [(x_pos * x, self.npc_y_pos) for x in range(5, 45)]

        def set_postition(self, pos_xy):
            self.pos_xy = pos_xy

        def create_positions(self, x_pos):
            positions_player = []
            y_pos_boost = 0
            for row in range(3):
                positions_player += [(x_pos * x, self.player_y_pos + y_pos_boost) for x in range(5, 10)]
                y_pos_boost += 30
            return positions_player

        def mouse_is_over(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if self.pos_xy[0] < pos[0] < self.pos_xy[0] + self.width:
                if self.pos_xy[1] < pos[1] < self.pos_xy[1] + self.height:
                    return True
            return False

    class ShieldZone:
        def __init__(self):
            pass

        def create_slots(self, pos_xy):
            # creating slots for cards in the shield zone from a start position.
            shield_slots = [(pos_xy[0] * x, pos_xy[1]) for x in range(5, 45)]
            return shield_slots

    class Graveyard:
        def __init__(self):
            self.pos_xy = (0, 0)

            # size of a card.
            self.width = percent_of_screen_width(5.3)
            self.height = percent_of_screen_height(12.7)

        def set_position(self, pos_xy):
            self.pos_xy = pos_xy

        def mouse_is_over(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if self.pos_xy[0] < pos[0] < self.pos_xy[0] + self.width:
                if self.pos_xy[1] < pos[1] < self.pos_xy[1] + self.height:
                    return True
            return False


zones_class = Zones()