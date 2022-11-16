# # arr=['bc','xyz','aba','1221']
# # count=0
# # for i in arr:
# #     if len(i)>2 and i[0] == i[-1]:
# #         count+=1
# # print(count)
# #
# #
# # arr = list(range(1,101))
# # arr_sq = []
# # for i in arr[:5]:
# #     arr_sq.append(i*i)
# #
# # for i in arr[-5:]:
# #     arr_sq.append(i * i)
# # print(arr_sq)
#
# board = list(range(-2, 9))
# board1 =['X', 1, 2, 3, 'X', 'O', 6, 7, 'X']
# x = 1
# for i in board1:
#     end = " | "
#     if x % 3 == 0:
#         end = '\n---------\n'
#     char = ' '
#     if i in ['X', 'O']:
#         char = i
#     x += 1
#     print(char, end=end)
# print("Najib is win")
#
# # Assignment get input from user and complete the game.

# name='Najib'
# n1=[char.upper()for char in name]
# print(n1)
#
# friends=['Obiad','ali','yousf']
# f1=[friends[0].upper() for friend in friends]
# print(f1)

# #print even number
# arr= list(range(1,100))
# even= [i for i in arr if i%2==0]
# #print else if print event else odd
# eo=[i if i%2==0 else i/2 for i in arr]
# print(eo)
#
# string='this is so mucth fun'
# t="".join([char for char in string if char not in 'aeiou'])
# print(t)

# num=int(input("how mucth km do you want to run :"))
# rezult=num/1.6
# print(f"{num} km is = {rezult} in mile")

for i in range(6):
    for j in range(1,-i-1):
        print(end='')
    for j in range(1,i+1):
        print("\U0001f600")


