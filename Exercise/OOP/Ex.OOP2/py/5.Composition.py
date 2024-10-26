
#? Football team management system
class Player:
    def __init__(self, name, position, goals):
        self.name = name
        self.position = position
        self.goals = goals

class Coach:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.coach = None

    def add_player(self, player):
        self.players.append(player)

    def set_coach(self, coach):
        self.coach = coach

# Example of creating a team
team = Team("Thailand National Team")
coach = Coach("Coach Yod", "4-4-2")
team.set_coach(coach)
player1 = Player("Somchai", "Forward", 10)
team.add_player(player1)

# Optional: Print team details
print(f"Team: {team.name}")
print(f"Coach: {team.coach.name}, Strategy: {team.coach.strategy}")
print("Players:")
for player in team.players:
    print(f"{player.name} - Position: {player.position}, Goals: {player.goals}")

