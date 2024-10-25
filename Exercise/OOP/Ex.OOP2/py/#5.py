
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

team = Team("ทีมชาติไทย")
coach = Coach("โค้ชยอด", "4-4-2")
team.set_coach(coach)
player1 = Player("สมชาย", "กองหน้า", 10)
team.add_player(player1)
