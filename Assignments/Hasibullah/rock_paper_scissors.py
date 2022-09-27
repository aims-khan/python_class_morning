# Rock Paper Scissors game by Hasibullah
import random
play_again = True
arr = ['rock','paper','scissors']
while play_again:
    print("Select YOur Move\nRock\nPaper\nScissors")
    p1 = input("Select your move: ")
    if p1 in arr:
        p2 = random.choice(arr)
        print(f"Computer Choice is : {p2}")
        if p1.lower() == p2.lower():
            print("Equal")
        if p1.lower()=="rock":
            if p2.lower()=="paper":
                print("Computer Won")
            elif p2.lower()=="scissors":
                print("You Won")
        elif p1.lower()=="paper":
            if p2.lower()=="rock":
                print("You Won")
            elif p2.lower()=="scissors":
                print("Computer Won")
        elif p1.lower()=="scissors":
            if p2.lower()=="rock":
                print("You Won")
            elif p2.lower()=="paper":
                print("You Won")
        else:
            print("Wrong Input")
    else:
        print("Wrong Input")
    a = input("Do You Play Again? Y/N: ")
    if a[0].lower() == "y":
        play_again = True
    else:
        play_again = False