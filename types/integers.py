# Типы данных чисел -> int, float

# = -> оператор присваивания
# variable(переменная)
# num = 5 #5
# print(num)
# num = 79  # переопределенние
# print(num) #79

# abc  -> нижний регистр
# ABC  -> верхний регистр

# PEP8
# tommorow_day = "10.03.2023" # Snake Case
# tommorowDay = "10.03.2023" # Camel Case

# num1 = 5
# num2 = 15
# result = num1 + num2

# print('Summa:', result)

# # -
# num1 = input("Enter the num1:")
# num2 = input("Enter the num2:")
# num1 = int(num1)
# num2 = int(num2)
# print(num1 - num2)
# print(num2, '-',num1,'=',num2-num1)

# * - умножения
# num1 = int(input('Enter the num1: '))
# num2 = int(input('Enter the num2: '))
# print(num1, '*',num2,'=',num1*num2)


# / and // and %
# / - обычное деление
# // - деление без остатка
#  % - модульное деление(получение остатка от деления)

# num1 = 7
# num2 = 3
# print('/', num1 / num2) #2.33333....
# print('//', num1 //num2) # 2
# print('%', num1 % num2) # 1

# ** ->  возведение в степень
# print(5 ** 2)
# print(16 ** 55)

# print(9 ** 0,5) # квадратный корень

# pow - возведение в степень
# pow(num1, num2, <mod>)
# print (pow(5,10,65))
# print (5 ** 10 % 65)

# a = 5
# b = 2
# res = pow(a,b,12)
# print(res)

# round() - округления числа с плавающей точкой
# a = 5.6768786
# print(round(a, 3))

# abs() - абсолютное значение числа -> abs(-5) -> 5
#                                         |-5| -> 5

# a = abs(-16)
# b = abs(15)
# print(a,b)

# divmod(a,b) -> она выводит два числа, первое 
# число это результат целочисленного деления(//)
# a  на b, а второе  это модульное деление(%)

# res = divmod(5,2) 
# print(res)
# print((5 // 2, 5 % 2))

# import math
# a = 5
# print(round(math.sqrt(a), 2))

# res = math.sqrt(a)
# print(round(res, 2))

# # множественнон присваивание
# # оператор присвание(=)
# a = 5
# b = 15
# c = None

# print('a:',a,'b:',b)

# # c = a
# # a = b
# # b = c
# a, b = b, a
#         # 15, #5
# print('a:',a,'b:',b)

# num1, num2, num3 = input('num1: '), input('num2: '), input
# ('num3: ')
# print(num1)
# print(num2)
# print(num3)

# print(pi, type(pi))
# import math
# print(math.pi)

# from math import pi      

# r = int(input('Vvedite radius: '))
# res_P = 2 * r * pi
# res_S = pi * r ** 2
# print("S okruzhnosti: ", round(res_S, 2))
# print("P okruzhnosti: ", round(res_P, 2))

# from random import randint

#  print(randint(1,10))
# name = input('Vvedite svoe imya:')
# last_name = input('Vvedite svoyu familyu: ')
# num = randint(1000000, 9999999)
# print(name,last_name, num)
# res = name + last_name + str(num)
# print(res)

# from random import randint

# num = randint(1,10)
# print(num)
# i = 0
# while i < 3:
#    guess = int(input('Ugadai chislo:'))
#    if guess == num: 
#       print('Ty Pobedil! Krasava')
#       break
#     # i = i + 1 
# i += 1 #increment 



















