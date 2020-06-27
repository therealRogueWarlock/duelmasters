if len(self.cards_in_mana_zone) >= 1:

    available_mana = len(self.cards_in_mana_zone)

    lowest_mana_cost = 0

    while available_mana >= lowest_mana_cost:

        lowest_mana_cost = 10

        for card in self.cards_in_hand:
            if card.mana_cost < lowest_mana_cost:

                lowest_mana_cost = card.mana_cost
                print(card.name)
                self.picked_up_card = card

                if available_mana >= lowest_mana_cost:
                    for i in range(lowest_mana_cost):
                        self.cards_in_mana_zone[i].is_clicked()
                        self.float_mana(self.cards_in_mana_zone[i])
                    available_mana -= self.picked_up_card.mana_cost
                    self.play_card()