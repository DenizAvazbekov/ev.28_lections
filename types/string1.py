'String - Строки'
'hello world true 5 none'

"""
Hello world
my name is John Snow
"""

'''
Hello
world s vami kani
'''

# Строки - Набор последовательных символов, которые мы используем для
#  хранения и представления текстовой информации

# Индексация в строке
# name = 'John'
#     # J = 0 = -4
#     # o = 1 = -3
#     # h = 2 = -2
#     # n = 3 = -1
# print(name)
# print(name[1])
# str1 = 'kani1'
# print(str1[-1],str1[0])

# str1 = 'birthday'
# # print(str1[5], str1[6], str1[7])
# # print(str1[0],str1[1],str1[2],str1[3],str1[4])

# print(str1[5] + str1[6] + str1[7])
# print(str1[0] + str1[1] + str1[2]+ str1[3]+ str1[4])

# Срезы по индексам
# [start: end: <step>]

# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])

# text = 'hello world! my name is john! I\'m King of North '
# # print(text[:13])
# # print(text[::2])
# print(text[::-1])


# Конкатенация строк(соединения)

# a = 'Hello'

# b = 'world'

# c = ''

# print(a + c + b)

# экранирование - способ записи символов в строку, которые невозможно ввести
# с клавиатуры

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция 
# \f -> перевод страницы
# \r -> возврат указателя
# print('\vHello \tworld!\nMy name is John Snow!')

# Форматирование строк
# 1. с помощью %
# 2. с использованием .format()
# 3. Интерполяции строк (преобразование, f-stroki)


# %
#  name =  input ('Vvedite imya:')
#  last_name = input('Vvedite last_name:')
# print('Добро пожаловать к нам ' + name + ' ' + last_name + '!')
# print('Hello mr/mrs %s %s!' %(name, last_name))

#.format
# name =  input ('Vvedite imya:')
# last_name = input('Vvedite last_name:')
# club = 'Lanispot'
# print('Привествую вас, {} {}, в наш клуб {}!'.format(name, last_name, club))

# f-stroki
# a = input('Enter mr/mrs:')
# name = input('Vvedite imya: ')
# last_name = input('Vvedite last_name: ')
# print(f'Hello {a} {name} {last_name}! Welcome to the parthy')

# text = 'Запомни Питтер, с большой силой приходит и большая ответственность.'
# reversed_text = text[::-1]
# print(reversed_text)
# i = 0
# count_t = 0
# len_text = len(reversed_text)
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == 'т' or symbol == "Т":
#         count_t += 1
#     # print(symbol)
#     i += 1

# print(f'В тексте "т" встретилась {count_t} раз!')

