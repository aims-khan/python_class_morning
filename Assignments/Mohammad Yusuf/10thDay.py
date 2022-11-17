import random


def flip_coin():
    if random.random() > 0.5:
        return "HEADS"
    return "TAILS"

print(flip_coin())

 
