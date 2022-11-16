# tuple values are constant 
from ast import Index


months = ('January','Feb')

# print(months)
# print(months[0])

# for i in months:
#     print(i)
months.count(2)
months.index('January')

a = (1,2,3,(4,5),6)

for i in a:
    if not isinstance (i, int):
        for j in i:
            print(j)
    else:  
         print(i)
join1=""
b = 'join the text'

for j in b:
    join1 +=''.join(j)
print(join1)


s = {1,2,3,4,5,6}
print(s)
s.remove(6)
print(s)

ab = {1,2,3,4,5}
ba = {4,5,6,7,8}

Or = ab | ba
And =ab & ba

print(Or)
print(And)

# pip3 install pygame
# pip install pygame