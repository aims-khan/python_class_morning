# assignment 1
List1 = ['KBL', 'GZN', 'PRWN']
List2 = ['Kabul', 'Ghazni', 'Parwan']

mach = {List1[i]:List2[i]  for i in  range(0,3) }

print(mach)


# assignment 2 :

alphabit = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

vowel = ['a','e','i','o','u']

vowelDic = {i:0 for i in alphabit if i in vowel }
print(vowelDic)


 