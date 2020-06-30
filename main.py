import pygame
import time
import threading
import sys


# main class handel starting, stopping and the different loops for the game.
class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()

        # ticks used to slow down npc phases of turn, without stopping blitting and player input.
        self.get_ticks = pygame.time.get_ticks
        self.npc_turn_start_time = 0
        self.npc_turn_time = 0

        self.double_click_clock = pygame.time.Clock()
        self.wait_time = 500
        self.running = False
        self.tick_rate = 144

    def start(self):
        self.running = True
        print('starting game')
        self.startscreen_loop()
        self.game_loop()

    def startscreen_loop(self):
        pass

    def game_loop(self):
        while self.running:
            self.clock.tick(self.tick_rate)
            self.player_take_turn()
            self.npc_take_turn()

    def check_player_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            active_cards = player.get_interactive_cards() + npc.cards_in_battle_zone + npc.shields

            # all cards on battlefield can be hovered over to get info.
            for card in active_cards + npc.cards_in_mana_zone:
                card.mouse_is_over(player.mouse_pos())

            player.manage_cards_in_hand()

            # if the mouse is clicked check if mouse is over a card or button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in reversed(active_cards):
                    if not player.picked_up_card:
                        if card.mouse_is_over(player.mouse_pos()):
                            card.is_clicked()

                            if self.double_click_clock.tick() < self.wait_time:
                                if player.current_phase == "attack":
                                    if card in player.cards_in_battle_zone:
                                        card.is_double_clicked()
                                        player.selected_card = card
                                        print(player.selected_card.name, card.owner)

                                    if card in npc.cards_in_battle_zone + npc.shields:
                                        card.is_clicked_bool = True
                                        player.target_card = card

                                        print(player.target_card.name, card.owner)

                            if card.in_mana_zone:
                                player.float_mana(card)  # self.player will float mana from the card if not tapped.
                            if card.in_hand:
                                player.picked_up_card = card

            if event.type == pygame.MOUSEBUTTONUP:
                if zones_class.manazone.mouse_is_over(player.mouse_pos()):
                    if player.picked_up_card:
                        if player.current_phase == "charge":
                            if not player.if_charged_mana:
                                player.put_card_in_mana_zone()
                            else:
                                print("you can only charge mana once per turn.")
                        else:
                            print('you can only charge mana when in charge step.')

                if zones_class.battlezone.mouse_is_over(player.mouse_pos()):
                    if player.picked_up_card:
                        if not player.picked_up_card.in_battle_zone:
                            if player.current_phase == "main":
                                player.play_card()
                            else:
                                print('you can only play a card when in main step.')

                for card in active_cards:  # if mouse not clicked, no card is picked up.
                    card.is_picked_up = False
                    player.picked_up_card = None
                    player.position_cards_in_hand()

                # checking if a button is clicked, and what button.
                for button_name in all_buttons:
                    button = all_buttons[button_name]
                    if button.is_over(player.mouse_pos()):

                        if player.current_phase is not None:  # player can only click the button if its players turn.
                            if button.text == "next":
                                player.next_phase()

                        if button.text == "attack":
                            if player.target_card.in_shield_zone:
                                npc.put_shield_in_hand(player.target_card.pos_index)

                            else:
                                player.selected_card.fight(player.target_card)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_w:  # draw a card
                    player.draw_a_card()

                if event.key == pygame.K_r:
                    npc.setup()
                    player.setup()

                if event.key == pygame.K_t:
                    player.shuffle_back_cards()
                    npc.shuffle_back_cards()

                if event.key == pygame.K_s:
                    player.shuffle_deck()

                if event.key == pygame.K_i:
                    print(player.player_info())

    def npc_check_for_events(self):

        if npc.current_phase == "untap":
            if self.npc_turn_time >= self.npc_turn_start_time + 1000:
                npc.next_phase()

        if npc.current_phase == "draw":
            if self.npc_turn_time >= self.npc_turn_start_time + 2000:
                npc.next_phase()

        if npc.current_phase == "charge":
            if self.npc_turn_time >= self.npc_turn_start_time + 3000:
                npc.next_phase()

        if npc.current_phase == "main":
            if self.npc_turn_time >= self.npc_turn_start_time + 5000:
                npc.next_phase()

        if npc.current_phase == "attack":
            if self.npc_turn_time >= self.npc_turn_start_time + 6000:
                npc.next_phase()

        if npc.current_phase == "end":
            if self.npc_turn_time >= self.npc_turn_start_time + 7000:
                npc.next_phase()

    def player_take_turn(self):
        print(f"start {player.name}'s turn")
        player.next_phase()
        while player.current_phase is not None:
            self.clock.tick(self.tick_rate)
            blit_game.blit_window()
            self.check_player_events()
        print(f"end {player.name}'s turn")

    def npc_take_turn(self):
        print(f"start {npc.name}'s turn")
        npc.next_phase()
        self.npc_turn_start_time = self.get_ticks()
        while npc.current_phase is not None:
            self.clock.tick(self.tick_rate)
            self.npc_turn_time = self.get_ticks()
            self.npc_check_for_events()
            self.check_player_events()
            blit_game.blit_window()
        print(f"end {npc.name}'s turn")

    def pause(self):
        pass

    def shutdown(self):
        pass


main_class = Main()

if __name__ == "__main__":
    pygame.init()
    from blit import blit_game
    from zones import zones_class
    from players import player, npc
    from buttons import all_buttons

    main_class.start()
