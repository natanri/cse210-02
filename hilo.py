from pyclbr import Class
import random
Points = 300
# TODO: Implement the Die class as follows...
class pick_a_card:
    def __init__(self):
        self.value = 0
        self.point = Points
    def Player(self):
        print(self.point)
        self.value = random.randint(1, 13)
        print(f"the card is {self.value}")
class game:
    def __init__(self):
        self.guess = input("Higher or lower? [h/l] ")
    def guess_card(self, Player):
        print()
        if self.guess == "l":
           print(pick_a_card.Player.value(self))
