#  This module contains calsses for controlig a turn in game.


class Turns:
    def __init__(self):
        pass

    def untap_phase(self, player):
        # will untap all players card / reset player for start of turn.
        for card in player.get_interactive_cards():
            card.is_tapped = False

    def draw_phase(self, player):
        # will make the player draw a card.
        player.draw_a_card()
        pass


turn_manager = Turns()

