import random


class Die:
    
    def __init__(self, sides):
        self.sides = sides
        self.__value = 0

    def roll(self):
        self.__value = random.randint(1,self.sides)

    def get_value(self):
        return self.__value


class Player:

    def __init__(self, name):
        self.name = name
        self.__dice = list()

    def add_die(self, sides):
        self.__dice.append(Die(sides))

    def roll_dice(self):
        for die in self.__dice:
            die.roll()

    def get_dice_value(self):
        dice_value = 0
        for die in self.__dice:
            dice_value += die.get_value()

        return dice_value
    
    def get_number_of_dice(self):
        return len(self.__dice)


# The game itself #
if __name__ == "__main__":

    player = Player(input("Choose your name:"))

    for _ in range(int(input("Select the number of 6-sided dice to play with:"))):
        player.add_die(6)

    num_rounds = int(input("Select the number of rounds to play:"))

    score = 0

    for round in range(num_rounds):
        player.roll_dice()

        print("Round " + str(round))
        print("You scored:")
        print(player.get_dice_value())

        score += player.get_dice_value()

    print("Total score:")
    print(score)




