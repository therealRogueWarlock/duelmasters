# This module will contain classes for the zones. might not make sens to make.
import pygame
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)


class Zones:
    def __init__(self):
        self.x_pos = int(screen_size[0]*0.0625)  # the overall x-position of a zone on the screen.
        self.manazone = self.ManaZone(self.x_pos)
        self.shieldzone = self.ShieldZone(self.x_pos)
        self.battlezone = self.Battlezone(self.x_pos)

    class Battlezone:
        def __init__(self, x_pos):
            # Battle zone
            # creating postions for cards in players battlezone
            self.pos_xy = (x_pos * 5, int(screen_size[1] * 0.46))

            self.height = int(screen_size[1] * 0.125)

            self.width = int(screen_size[0] * 0.31)

            self.rect = (self.pos_xy[0], self.pos_xy[1], self.width, self.height)

            self.player_y_pos = int(screen_size[1] * 0.46)

            self.positions_player = [(x_pos * x, self.player_y_pos) for x in range(5, 45)]

            # creating positions for cards in npc battlezone
            self.npc_y_pos = int(screen_size[1] * 0.3)
            self.positions_npc = [(x_pos * x, self.npc_y_pos) for x in range(5, 45)]

        def mouse_is_over(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates.
            if self.pos_xy[0] < pos[0] < self.pos_xy[0] + self.width:
                if self.pos_xy[1] < pos[1] < self.pos_xy[1] + self.height:
                    return True
            return False

    class ManaZone:
        def __init__(self, x_pos):
            # Mana zone
            # creating postions for cards in players manazone
            self.pos_xy = (x_pos*5, int(screen_size[1]*0.741))

            self.height = int(screen_size[1] * 0.125)

            self.width = int(screen_size[0] * 0.31)

            self.rect = (self.pos_xy[0], self.pos_xy[1], self.width, self.height)

            self.player_y_pos = int(screen_size[1]*0.741)

            self.positions_player = self.create_positions(x_pos)

            # creating positions for cards in npc manazone
            self.npc_y_pos = int(screen_size[1]*0.052)
            self.positions_npc = [(x_pos * x, self.npc_y_pos) for x in range(5, 45)]

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
        def __init__(self, x_pos):
            self.player_y_pos = int(screen_size[1]*0.602)  # 650
            # creating positions for cards in players shieldzone
            self.positions_player = [(x_pos * x, self.player_y_pos) for x in range(5, 45)]

            # creating positions for cards in npc shieldzone
            self.npc_y_pos = int(screen_size[1]*0.2)
            self.positions_npc = [(x_pos * x, self.npc_y_pos) for x in range(5, 45)]


zones_class = Zones()
