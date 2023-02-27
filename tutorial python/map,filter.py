# number = ['3','34','64']

# # for i in range(len(number)):
# #     number[i] = int(number[i])

# number= list(map(int, number))


# number[2] = number[2] + 1
# # print(number[2])

# # def sq(a):
# #     return a*a

# # num = [2,3,4,5,6,7,8,9,10]
# # square = list(map(sq, num))
# # print(square)

# num = [2,3,4,5,6,7,8,9,10]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# num = [2,3,4,5,6,7,8,9,10]
# func = [square, cube]

# for i in range(5):
#     val = list(map(lambda x: x(i) , func))
#     print(val)


# ........................ filter ................
# list_1 = [1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5, list_1))
# print (gr_than_5)

# ............. reduce .................
from functools import reduce

list_2 = [1,2,3,4,5]
# num = 0 
# for i in list_2:
#     num = num+i
# print (num)

num = reduce(lambda x,y: x+y, list_2)

print(num)
# print ((8*60)/18)