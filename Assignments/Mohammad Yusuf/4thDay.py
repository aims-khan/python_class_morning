import random
statEnd = input("enter start to start the and end for end the program enter 'end': ")
sm = input("'single' for single player 'multi' for multi player: ")
arr = ['rock', 'paper', 'scissors']
if statEnd == "start":
    if sm == "single":
        while statEnd == "start":
            Player1 = input("Player 1, make your move: ")
            Player2 = random.choice(arr)

            print("Computer choice: ", Player2)
            if Player1 == "rock" and Player2 == "scissors":
                print("Player 1 wins")
            elif Player1 == "rock" and Player2 == "paper":
                print("Player 2 wins")
            elif Player1 == "paper" and Player2 == "rock":
                print("Player 1 wins")

            elif Player1 == "paper" and Player2 == "scissors":
                print("Player 2 wins")
            elif Player1 == "scissors" and Player2 == "rock":
                print("Player 2 wins")
            elif Player1 == "rock" and Player2 == "rock":
                print("Player 1 and 2  are equal.")
            elif Player1 == "scissors" and Player2 == "scissors":
                print("Player 1 and 2  are equal.")
            elif Player1 == "paper" and Player2 == "paper":
                print("Player 1 and 2  are equal.")
            elif Player1 == "scissors" and Player2 == "paper":
                print("Player 1 wins")
            else:
                print("wrong input!!!")
            statEnd = input("enter start to start the and end for end the program enter 'end': ")
            sm = input("'single' for single player 'multi' for multi player: ")
    elif sm == "multi":
              while statEnd == "start":
                    Player1 = input("Player 1, make your move: ")
                    Player2 = input("Payer2, make your move: ")
                    if Player1 == "rock" and Player2 == "scissors":
                        print("Player 1 wins")
                    elif Player1 == "rock" and Player2 == "paper":
                        print("Player 2 wins")
                    elif Player1 == "paper" and Player2 == "rock":
                        print("Player 1 wins")

                    elif Player1 == "paper" and Player2 == "scissors":
                        print("Player 2 wins")
                    elif Player1 == "scissors" and Player2 == "rock":
                        print("Player 2 wins")
                    elif Player1 == "rock" and Player2 == "rock":
                        print("Player 1 and 2  are equal.")
                    elif Player1 == "scissors" and Player2 == "scissors":
                        print("Player 1 and 2  are equal.")
                    elif Player1 == "paper" and Player2 == "paper":
                        print("Player 1 and 2  are equal.")
                    elif Player1 == "scissors" and Player2 == "paper":
                        print("Player 1 wins")
                    else:
                        print("wrong input!!!")
                    statEnd = input("enter start to start the and end for end the program enter 'end': ")
                    sm = input("'single' for single player 'multi' for multi player: ")
    else:
                print("wrong input!!!")



else:
    print("Game over.")



arr234 = [1,2,3,4]
print(arr234.reverse())