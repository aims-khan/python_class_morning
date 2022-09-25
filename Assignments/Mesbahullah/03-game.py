import random

arr =["rock","paper","scissors"]

play_again = True
while play_again:
    print("rock")
    print("scissors")
    print("paper")
    You = input("Select your move. ")

    # person2 = input("Select your move. ")

    Computer = random.choice(arr)
    print("Computer choice: ", Computer)

    if You =="rock" and Computer == "paper":
        print("Computer is win..")

    elif  You == "scissors" and Computer == "paper":
        print("You is win...")

    elif You == "paper" and Computer == "scissors":
        print("Computer is win...")

    elif Computer == "rock" and  You == "scissors":
        print("Computer is win...")

    elif  You == "rock" and Computer == "rock":
        print("both are equal..")

    elif   You == "paper" and Computer =="paper":
        print("both are equal..")
    elif   You == "paper" and Computer =="rock":
        print("You win")

    elif You == "scissors" and Computer =="scissors":
        print("both are squal...")

    else:
        print("you are not start yet")
        print("would you like to play again..")

    a = input("Do u Play Again Y/N: ")
    if a.lower() == "y":
        play_again = True
    else:
        play_again = False
        print("good luck guys...")

# arr =["rock","paper","scissors"]
# import random
# rand_choice = random.choice(arr)

# if rand_choice == "rock":
#     computer = "rock"
# elif rand_choice == "paper":
#     computer = "paper"
# else 



