from Controller import PlayerController

if __name__ == "__main__":
    controller = PlayerController()

    controller.add_player(1, "Virat Kohli", "RCB", "Batsman", runs=500)
    controller.add_player(2, "Jasprit Bumrah", "MI", "Bowler", wickets=25)

    controller.update_player_stats(1, runs=50)
    controller.update_player_stats(2, wickets=2)

    controller.show_all_players()

    controller.top_scorer()
    controller.top_wicket_taker()
