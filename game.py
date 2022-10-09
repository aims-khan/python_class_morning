#this is code is not allowed for copy so sorry 
for i in range(5):
    print('\U0001f600'*1)
arr = list(range(1,31))
result =[]
for i in arr[:5]:
    result.append(i*i)
for i in arr[-5:]:
    result.append(i*i)
print(result)
#this section is related with game
board = list(range(-2,9))
board1 = ['X',1,2,3,'X','O',6,7,'O']
X=1
for i in board1:
    end = " | "
    if X%3 == 0:
        end = '\n------------\n'
    char = " "
    if i in ['X', 'O']:
        char = i
    X+=1
    print(char, end=end)
