# it dosn't has order it store data rundomly
from multiprocessing.sharedctypes import Value


dictionary = {
    'name': 'Yusuf',
    'age': 22,
    'bp': 'Pakistan'
}

print(dictionary.items())

# Note: for i in dictionary.keys = for i in dictionary
for j in dictionary.values():
    print(j)

for k,v in dictionary.items():
    print(k,v)
# clear data of dictionary
# dictionary.clear()

dictionary1 = dictionary
# this is best practice becuase it gives error when key is not found bellow dosn't
# dictionary['name']

# dictionary.get('name')

#we should assign key to pop it other wise it give error
# dictionary.pop('name')
# print(dictionary)

# pop randomly
# dictionary.popitem()
# print(dictionary)

dictionary.update({'name': 'Yusuf Khan'})
print(dictionary)


Insturactor ={
    'name': 'ali',
    'have_master': True,
    'favorite': 'python',
    'other_uni': False
}

for k,v in Insturactor.items():
    print("Your key is: "+ str(k) + " and your value is: "+ str(v))

arr = [1,2,3,4,32,5,6,23,7]
nums = {i: i**2 for i in arr }
print(nums)


str1 = "ABCD"
str2 = "1234"

string =  {str1[i]:str2[i] for i in range(0,4) }
print(string)


dic = {'name':'abc', 'city': 'kabul', 'country': 'afghanistan'}

dic1 = {i:j.upper() for i,j in dic.items() }
print(dic1)


arr12 = [1,2,3,4,5]

oddeven = {i:('even' if  i %2 == 0  else 'odd') for i in arr12  }

print(oddeven)