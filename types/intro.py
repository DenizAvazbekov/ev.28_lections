#Типы данных в питоне 

# 1.NoneType - ничего, пустота -> None 

# 2. Boolean - истинна или ложь -> True/False

# 3. String - строки - str -> "Hello World", 'Hello World'

# 4. Числовые типы данных

    # a) integer - целое число int -> -1, 2, 555

    # b) float - число с плавающей точки -> 1.5, 15.25

    # c) complex - 0j:1, 5-9j

# 5.Списковые типы данных (коллекция)

    # a) list(массив/список) -> [5, 2 ,4 True, False, 'hello']

    # b) tuple(кортеж) -> (1, 2, 3, None)

    # c) range(последавтельность) -> range(1, 10) 

# 6. set() - множество -> {1,2,3,4,5,6,7,8} 

# 7. dict(словари) -> содержат данные в себе в виде ключа и значение { 1: "one", 2: "two"}

# mutable(изменяемые типы данных)

    # 1. list

    # 2. set

    # 3. dict 

# Immutable(неизменямые типы данных)

    # 1. None

    # 2. bool

    # 3. int, float, complex

    # 4. str

    # 5. tuple, range

    # 6.frozenset  
    
# Переменная - проименованная область памяти, предназначенная для хранения данных. С её помощью мы можем проводить различные операции с данными

num = 5 
str1 = "Hello World"

'''

Стандартный вывод данных
'''

# в питоне для вывода данных в терминал использауется встроенная функция print()

stroka = "Hello World! My name is John Snow"
print(stroka)
print(27 + 5) 
 
'''
 стандартный ввод данных через терминал 
 изпользуется функция input() 
'''
 
# a = input("Введите число: ")
# num = int(a)
# # print(num)
# # print(type(num))
# # print("данные в переменных:" a, num)
# print("В переменной a хранится:", a, "ее тип данных", type(a))
# print("В переменно num хранится:", num, "ее тип данных", type(num))