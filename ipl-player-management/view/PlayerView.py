class PlayerView:
    def display_player(self, player):
        print("Player Details:")
        print(player.get_details())

    def display_all_players(self, players):
        print("\nAll Players:")
        for player in players:
            print(player.get_details())
