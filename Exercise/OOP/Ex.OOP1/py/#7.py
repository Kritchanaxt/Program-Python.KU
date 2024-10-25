
class MembershipCard:
    def __init__(self, member_name):
        self.member_name = member_name
        self.points = 0

    def add_points(self, points):
        if points > 0:
            self.points += points
            print(f"{points} points added. Total points: {self.points}.")
        else:
            print("Points to add must be positive.")

    def redeem_points(self, points):
        if 0 < points <= self.points:
            self.points -= points
            print(f"{points} points redeemed. Remaining points: {self.points}.")
        else:
            print("Invalid points to redeem.")

card = MembershipCard("Alice")
card.add_points(100)
card.add_points(50)
card.redeem_points(30)
card.redeem_points(200)  