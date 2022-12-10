a = [1,2,3,4,5]
print(a)
a.append(6)
print(a)
a.extend([7,8,9])
print(a)
a.insert(2,"hello")
print(a)
a.pop(2)
print(a)
a.remove(5)
print(a)
# a.clear()
# print(a)
print(a.index(4))
print(a.count(5))
a.reverse()
print(a)
a.sort()
print(a)
names = ['ali','ahmad','khalid']
print(" ".join(names))
print(a[:-1])
print(a[::2])
print(a[::-1])
a[2:2] = names
print(a)

#list comprehension
print([i*2 for i in a])
print([i if i%2==0 else i/2 for i in range(1,11) ])
print([[ num for num in range(1,4)] for val in range(1,4)])

# dictionary
d = {
    'name': 'ali',
    'age': 23,
    'is_single': True
}
print(d)

dd = dict(a=1,b=2,c=3)
print(dd)
dd = dict(d=4)
print(dd)
print(d['name'])
print(d.values())
print(d.keys())
print(d.items())
print('ali' in d.keys())
ddd = d.copy()
print(d)
print(ddd)
print(d is ddd)
print(d['age'])
print(d.get('age'))
print(d.pop('name'))
print(d.popitem())
print(dd.update(d))
print(dd)

# dictionary  comprehension
print({a : a*a for a in range(1,6)})
list1 = ['kbl', 'herat', 'mazar']
list2 = ['Kabul', 'Herat', "Balkh"]
print({ list1[i]: list2[i] for i in range(3)})