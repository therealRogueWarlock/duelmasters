import pygame
import sys


# main class handel starting, stopping and the different loops for the game.
class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.double_click_clock = pygame.time.Clock()
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
            self.player_take_turn()
            self.npc_take_turn()

    def check_player_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            active_cards = player.get_interactive_cards() + npc.cards_in_battle_zone

            for card in active_cards:
                card.mouse_is_over(player.mouse_pos())

            # if the mouse is clicked check if mouse is over a card or button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in reversed(active_cards):
                    if not player.picked_up_card:
                        if card.mouse_is_over(player.mouse_pos()):
                            card.is_clicked()

                            if self.double_click_clock.tick() < 500:

                                if player.current_phase == "attack":
                                    if card in player.cards_in_battle_zone:
                                        card.is_double_clicked()
                                        player.selected_card = card
                                        print(player.selected_card.name, card.owner)

                                    if card in npc.cards_in_battle_zone:
                                        card.is_double_clicked()
                                        player.target_card = card
                                        print(player.target_card.name, card.owner)

                            if card.in_hand:
                                # when the card is clicked it will be moved to the last pos in hand.
                                # This will make that card blit last, and stay ontop.
                                player.cards_in_hand.remove(card)
                                player.cards_in_hand.append(card)

                            if card.in_mana_zone:
                                player.float_mana(card)  # self.player will float mana from the card if not tapped.
                            else:
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

                # checking if a button is clicked, and what button.
                for button_name in all_buttons:
                    button = all_buttons[button_name]
                    if button.is_over(player.mouse_pos()):

                        if button.text == "next":
                            player.next_phase()

                        if button.text == "attack":
                            player.selected_card.fight(player.target_card)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_w:  # draw a card
                    player.draw_a_card()

                if event.key == pygame.K_r:
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
            npc.next_phase()

        if npc.current_phase == "draw":
            npc.player_info()
            npc.next_phase()

        if npc.current_phase == "charge":
            # TODO need more logic
            if len(npc.cards_in_mana_zone) < 5:
                max_mana_cost = 0
                for card in npc.cards_in_hand:
                    if card.mana_cost > max_mana_cost:
                        max_mana_cost = card.mana_cost
                        npc.picked_up_card = card
                npc.put_card_in_mana_zone()
            npc.next_phase()

        if npc.current_phase == "main":
            if len(npc.cards_in_mana_zone) > 1:
                low_mana_cost = 0
                for card in npc.cards_in_hand:
                    if card.mana_cost > low_mana_cost:
                        low_mana_cost = card.mana_cost
                        npc.picked_up_card = card
                npc.play_card()
            npc.next_phase()

        if npc.current_phase == "attack":
            npc.next_phase()

        if npc.current_phase == "end":
            npc.next_phase()

    def player_take_turn(self):
        print(f"start {player.name}'s turn")
        player.next_phase()
        while player.current_phase is not None:
            self.clock.tick(self.tick_rate)
            blit_game.blit_window()
            self.check_player_events()
        print(f"end {player.name}'s turn")
        player.turn_counter += 1

    def npc_take_turn(self):
        npc.next_phase()
        while npc.current_phase is not None:
            self.clock.tick(self.tick_rate)
            blit_game.blit_window()
            self.npc_check_for_events()
        player.turn_counter += 1

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
