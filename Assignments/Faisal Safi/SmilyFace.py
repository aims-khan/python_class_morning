rows=7
for r in range(0,rows):
    for c in range(0,rows-r-1):
        print(" ",end="")
    for c in range(0,r+1):
        print("😒",end=" ")
    print()
print()
for j in range(10):
    print("")
    for i in range(j):
        print("😒",end=" ")
for j in range(10,0,-1):
    print("")
    for i in range(j):
        print("😒",end=" ")