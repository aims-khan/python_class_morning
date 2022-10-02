import random
again=True
while again:
    p1=input("Enter you Move: ")
    rand_num=random.randint(1,3)
    if rand_num==1:
        com="rock"
    elif rand_num==2:
        com="paper"
    else:
        com="scissors"
    print("computer has selected: "+com)
    if p1.lower()==com.lower():
        print("Try Again Same move Selected")
    if p1.lower()=="rock":
        if com=="paper":
            print("Computer Won")
        elif com=="scissors":
            print("You Won")
    elif p1.lower()=="paper":
        if com=="rock":
            print("You won")
        elif com=="scissors":
            print("Computer won")

    elif p1.lower()=="scissors":
        if com=="rock":
            print("Computer Won")
        elif com=="papar":
            print("You won")
    elif p1.lower()==com:
        print("same Selection")
    else:
        print("Wrong input ")
    a = input("Do you want to play again? Y/N: ")
    if a[0].lower() == "y":
        again = True
    else:
        again = False


