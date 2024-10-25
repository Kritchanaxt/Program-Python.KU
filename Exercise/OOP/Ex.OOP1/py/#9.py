import random

class Die:
    def roll(self):
        return random.randint(1, 6)

class Game:
    def __init__(self, dice_count):
        self.dice = [Die() for _ in range(dice_count)]

    def roll_dice(self):
        results = [die.roll() for die in self.dice]
        return results

game = Game(dice_count = 3) # Create a game with 3 dice 
roll_results = game.roll_dice()

print("Results of the dice rolls:", roll_results) 