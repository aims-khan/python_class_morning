# By Hasibullah
# Please don't copy my code
for i in range(2,11):
    for j in range(1,11):
        print(j, ' * ', i, ' = ', j * i)
    print("____________________")

a = int(input("> "))
for i in range(a):
    print("I'm printing")

for i in range(1,21):
    if i == 4 or i == 13:
        print(i,"unlucky")
    elif i % 2 == 0:
        print(i,"Even")
    elif i % 2 == 1:
        print(i,"Odd")

for i in range(6):
    print('\U0001f600'*i)

arr = [1,2,3,4,5]
r = 0
for i in arr:
    r = r+i
print(r)

arr = [1,2,3,4,25,6]
l=0
for i in arr:
    if i>l:
        l=i
print(l)

l = []
for i in list(range(1,1001)):
    if i%2!=0:
        l.append(i)
print(l)