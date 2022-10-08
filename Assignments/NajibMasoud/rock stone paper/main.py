print("Rock..............")
print("Paper.............")
print("Scisser...........")

palyer1=input("p1 move your action: ")
palyer2=input("p2 move your action: ")

if palyer1==palyer2:
    print("Draw Game")

if palyer1=="rock"and palyer2=="paper":
    print("player1 is win")
elif palyer1 == "rock" and palyer2 == "scisser":
    print("player2 is win")
elif palyer1 == "paper" and palyer2 == "rock":
    print("player1 is win")
elif palyer1 == "paper" and palyer2 == "scisser":
    print("player2 is win")
elif palyer1 == "scisser" and palyer2 == "rock":
    print("player1 is win")
elif palyer1 == "scisser" and palyer2 == "paper":
    print("player1 is win")

else:
    print("Worng move try agin")
