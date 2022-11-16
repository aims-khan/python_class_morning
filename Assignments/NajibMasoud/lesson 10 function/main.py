import random


def flip_coin():
    r = random.random()
    print("the r value is: ",r)
    if r > 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flip_coin())
