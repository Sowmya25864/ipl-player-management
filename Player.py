class Player:
    def __init__(self, player_id, name, team, role, runs=0, wickets=0):
        self.player_id = player_id
        self.name = name
        self.team = team
        self.role = role
        self.runs = runs
        self.wickets = wickets

    def update_runs(self, runs):
        self.runs += runs

    def update_wickets(self, wickets):
        self.wickets += wickets

    def __str__(self):
        return f"ID: {self.player_id}, Name: {self.name}, Team: {self.team}, Role: {self.role}, Runs: {self.runs}, Wickets: {self.wickets}"
