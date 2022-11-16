# arr=list(range(0,100))
# even=[i for i in arr if i%2==0]
# print(even)
#
# even2=[i if i%2==0 else i/2 for i in arr]
# print(even2)
#
# for i in range(1,10):
#     print(" "+i*"*"+"")
#
# arr=list[1,2]
# print(type(list[1]))

#
# k=6
# for i in range(0,6):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for e in range(0,i+1):
#         print(" "+"*",end=" ")
#     print("\n")



# num=[[1,2,3],[2,3,5]]
#
# for j in num:
#     for k in j:
#         print(k)


arr1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
arr2=["a","e","i","o","u"]
arr3={i:"0" for i in arr1 for y in arr2 if i==y}
print(arr3)