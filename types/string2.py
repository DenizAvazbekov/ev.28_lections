# str
# ''
# 'Hello'
# str(5)

# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = 'John'
# print(a != b)
# print('abc' == 'abc')
# print(a > b)
# print(a < b)

# print('a') # 97 -> 1100001
# print('a'>'b') # 97 > 88
# print('h'>'c') # 104 > 99
# print('Hello' > 'Harry') #True
# print('abc' > 'abc') #False

# len() - возвращает кол-во символов в строке
# a = 'Hello'
# b = 'John Snow'
# print(len(a) <len(b))
# print(len(a), len(b))

# > < == != >= <=

# Методы строк
# replace (old, new, [count]) - меняет в строке символы old на new, если вы
# укажите count, то заменит count раз
# text = 'ha ha ha ha'
# result = text.replace('a', 'e', 2)
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello World! My name is John Snow!'
# res = str1.replace('John Snow', 'Tirion Lanister')
# print(res)

# strip() - Убирает пробельные символы в начале и в конце строки 
# rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
# print(dir(str))

# isdigit -         Проверяет
# isnumeric - -> состоит ли ваша строка
# isdecimal -    полностью
  
# num = input('Vvedite chislo: ')
# print(f'Vvedeno chislo?: {num.isdigit()}')

# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chisla!')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())

# isalnum() -> проверяет состоит ли наша строка из чисел 
# и символов латинкского алфавита и киррилицы
# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha -> состоит ли наша строка полностью из символов алфавита
# text = 'Hello World'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())

# islower()
# isupper()
# istitle()
# str1 = 'Ms. My Name '
# print(str1.islower())
# print(str1.istitle())
# str2 = 'RTY UIOP'
# print(str2.isupper())

# index(value, [start], [end]) - выводит индекс значения
# value, которые мы передаем, в нашей строке.
# text = 'Hello'
# print(text.index('l', 3))
# text = 'Hello john snow'
# print(text.index('john', 2,))
# text = 'Hello world! My name is John Snow!' #o
# print(text.index('John'))
# res = text.index('o')
# print(res)  #4
# res = text.index('o', res + 1)
# print(res)  #7
# res = text.index('o', res + 1)
# print(res)  #25
# res = text.index('o', res + 1)
# print(res)  #31

# text = 'hello o o o hello'
# prin(text.count('o'))
# prin(text.count('hello'))
# prin(text.count('ghj'))

# split(separator) - дробит нашу строку на несколько
# частей по разделителю все части сохраняются в типе list 

# text = "Let me speak by my hearth in English! Cause my name is John Snow"
# res = text.split(' ')
# print(res)
# print(len(res))

# a = 'hello#hello#hello#hello'
# res = a.split('#')
# print(res)

# 'connector'.join(list) -> соединяет по connector строки
# которые находились в list 

# text = "Let me speak by my hearth in English! Cause my name is John Snow!"
# res = text.split(' ')
# print(res)
# str1 = '#'.join(res)
# print(str1)

# find(value,[start],[end]) - делает тоже самое что и индекс но если не нашёл то вернется -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('lytui'), type(text.find('lytui')))
# print('John Snow')

#  swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
#  lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snownum = 1_000_000_000
# res = []

# for x in range(1, int(num ** 0.5)+ 1):
#     if num % x == 0:
#         res.extend({x, num // x})
# res.sort()
# print(res)

# print(f'Original:{text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitaliza() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f"Hello! Mr/Mrs {name}!")

# fio="john edart snow"
# print(fio.title())
# print(fio.capitalize())

# # print(dir(str))

















