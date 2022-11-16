
from ast import In
from cgitb import reset
from itertools import count


arr =  ['abc','xyz','ab','1221','ada','cvncnc']
result = 0
for i in arr:
    if len(i) > 2 and i[0] == i[-1]:
        result = result +1
        print(i)
print(result)

arr = list(range(1,101))
squre = []
for i in arr[:5]:
    
    squre.append(i *i)

for j in arr[-5:]:
    squre.append(j * j)

print (squre)      

for i in range(1,3):
    
    print("   ___|___|___")
    print("      |   |")

board = list(range(1,9))

for i in board:
    
    if (i+0)%3 == 0:
         end = '\n____________\n'
        
    else:
       end = "  |  "
    print(" ", end = end)

items = [1,2,3,2,2,2,4,5]

items.insert(len(items),12)
print(items)
# items.pop(3)
print(items)
# items.clear()
# items.remove(0)
# print(items)
# Index = items.index(23)
# print(Index)
# count1 = items.count(1212)
# print(count1)
items.reverse()
print(items)
items.sort()
print(items)
dep =set(items)
print(dep)
# ''.join(items)
nam = ['ahmad','walid']
naw =''.join(nam)
print(naw)