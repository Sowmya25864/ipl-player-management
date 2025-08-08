from Player import Player
from View import PlayerView

class PlayerController:
    def __init__(self):
        self.players = []

    def add_player(self, player_id, name, team, role, runs=0, wickets=0):
        player = Player(player_id, name, team, role, runs, wickets)
        self.players.append(player)
        PlayerView.display_message(f"Player {name} added successfully.")

    def update_player_stats(self, player_id, runs=0, wickets=0):
        for player in self.players:
            if player.player_id == player_id:
                player.update_runs(runs)
                player.update_wickets(wickets)
                PlayerView.display_message(f"Updated stats for {player.name}.")
                return
        PlayerView.display_message("Player not found.")

    def show_all_players(self):
        PlayerView.display_all_players(self.players)

    def top_scorer(self):
        if not self.players:
            PlayerView.display_message("No players available.")
            return
        top_player = max(self.players, key=lambda p: p.runs)
        PlayerView.display_message(f"Top Scorer: {top_player.name} with {top_player.runs} runs.")

    def top_wicket_taker(self):
        if not self.players:
            PlayerView.display_message("No players available.")
            return
        top_player = max(self.players, key=lambda p: p.wickets)
        PlayerView.display_message(f"Top Wicket-Taker: {top_player.name} with {top_player.wickets} wickets.")
