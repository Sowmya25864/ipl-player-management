# Player.py

class Player:
    def __init__(self, player_id, name, team, role, runs=0, wickets=0):
        self.player_id = player_id
        self.name = name
        self.team = team
        self.role = role
        self.runs = runs
        self.wickets = wickets
