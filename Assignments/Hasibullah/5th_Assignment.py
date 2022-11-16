
arr = [1,2,3,4,]

for i in arr:
    print(i)

for i in range(50,100,2):
    print(i, end='')
    print(i)



arr1 = range(1,100)
arr2 = arr1
print(arr1)
list(arr2)
print(arr2)

num = int(input("Enter some number: "))

for j in range(1,num+1):
    for i in range(1,11):
        print(i, '*' , j ,'=' ,j*i )


for i in range(1,21):
    if i == 4:
        print(str(i),"unlucky")
    elif i == 13:
        print(str(i), "unlucky")
    elif i % 2 == 0:
        print(str(i), "Even.")
   
    else :
        print(str(i),"odd.")


    # Assignment 1:
user = None
while user !='please' :
    user = input("Please say please: ")
emoji = "\U0001f600"
for i in range(1,10):
    
         print(emoji * i)

    # Assignment 2:
n = 6
k = n -1
for i in range(0, n):

    for j in range(0, k):
        print(end="  ")
    k = k - 1

    for m in range(0, i+1):
      print(emoji, end="  ")
    print("\n")

       


arrayOne = [1,2,3,4,5]
result = 0
for i in arrayOne:
    result += i
print(result)


result2 = 0
for i in  range(1,1000):
    result2 += i
print(result2)


arr3= [1,2,3,4,9,5,6,7]
num1 = 0
for i in arr3:
    
    num = i 
    if num > num1:
        num1 = num
print(num1)
