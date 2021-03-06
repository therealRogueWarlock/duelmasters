import pygame
import sys


# main class handel starting, stopping and the different loops for the game.
class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()

        # ticks used to slow down npc phases of turn, without stop blitting and player input.
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

            player.mouse_movement()

            # if the mouse is clicked check if mouse is over a card or button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.left_mouse_down()

            if event.type == pygame.MOUSEBUTTONUP:
                player.left_mouse_up()

                # checking if a button is clicked, and what button.
                for button_name in all_buttons:
                    button = all_buttons[button_name]
                    if button.is_over(player.mouse_pos()):

                        if player.current_phase is not None:  # player can only click the button if its players turn.
                            if button.text == "next":
                                player.next_phase()

                        if button.text == "attack":
                            player.selected_card.fight(player.target_card)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_w:
                    player.draw_a_card()

                if event.key == pygame.K_SPACE:
                    if player.current_phase is not None:  # player can go to next phase if its players turn.
                        player.next_phase()

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
            if self.npc_turn_time >= self.npc_turn_start_time + 500:
                npc.next_phase()

        if npc.current_phase == "draw":
            if self.npc_turn_time >= self.npc_turn_start_time + 1000:
                npc.next_phase()

        if npc.current_phase == "charge":
            if self.npc_turn_time >= self.npc_turn_start_time + 1500:
                npc.next_phase()

        if npc.current_phase == "main":
            if self.npc_turn_time >= self.npc_turn_start_time + 3000:
                npc.next_phase()

        if npc.current_phase == "attack":
            if self.npc_turn_time >= self.npc_turn_start_time + 4000:
                npc.next_phase()

        if npc.current_phase == "end":
            if self.npc_turn_time >= self.npc_turn_start_time:
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
