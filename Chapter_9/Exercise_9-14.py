from random import randint

class Die:
    """Modelling the dice."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(1, 11):
            x = randint(1, self.sides)
            print(x)

die1 = Die()
die1.roll_die()
print(" ")

die2 = Die(10)
die2.roll_die()
print(" ")

die3 = Die(20)
die3.roll_die()



