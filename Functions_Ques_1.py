import random

def roll_dice():
    return random.randint(1, 6)


def Ques_1():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")


Ques_1()
