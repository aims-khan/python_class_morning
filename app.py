import random
print("""select your move 
1:rock
2:paper
3:scissors""")
player1=input("player1, make your move:")
rand_num=random.randint(0,2)

if rand_num==0:
    computer="rock"
    print(f"computer choice {computer}")
elif rand_num==1:
    computer="paper"
    print(f"computer choice {computer}")
else:
    computer="scissors"
    print(f"computer choice {computer}")
if player1 == computer:
        print("==")
if player1=="rock"and computer=="scissors":
        print("player 1 wins")
elif player1=="rock"and computer=="paper":
        print("computer wins")
elif player1=="paper"and computer=="rock":
        print("player 1 wins")
elif player1=="paper"and computer=="scissors":
        print("computer wins")
elif player1=="scissors"and computer=="rock":
        print("player 1 wins")
elif player1=="scissors"and computer=="paper":
        print("player 1 wins")
elif player1=="rock"and computer=="rock":
        print("with this try you make me angry")
elif player1=="paper"and computer=="paper":
        print("wrong trying")
elif player1=="scissors"and computer=="scissors":
        print("with this try i will kick you")

b=input("Are you sure to palying again y/n")
if b[0.] =="y":
    play_again=True
else:
    play_again=false