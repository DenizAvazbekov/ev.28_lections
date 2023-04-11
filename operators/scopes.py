# Область видимости и пространства имен (scopes)
# технология которая определяет контекст имени 
# (переменные), в рамках которого мы можем ее ипользовать

# built-ins(Встроенная область видимости) -> print, len, max
# global(Глобальная) -> область одного файла
# enclosed(не локальная(замкунатая), nonlocal)
# local(локальная) -> область внутри одной функции

# x = 200
# def myFunc():
#     print(x)
#     a = 300
#     print(a)

# myFunc()
# print(a)
# print(x)

# a = 10 # global
# print # built-in
# def hello(): # global
#     a = 'Hello world'
#     print(a, 'local inside in func!')

# hello()
# print(a, 'global')

# LEGB - local enclosed global built-in
    # --------------->>>>>


#--------------------------------->
# Enclosed
# Замкнутое пространство имен - локальное пространство,
# у которого есть внутреннее(вложенное) локальное пространство

# x = 'global'
# print(x, '1')

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

# a = 5

# def func():
#     print(a)
#     a = a + 1
# func()

# global -> позволяет изменять значение глобальной
# переменной находясь внтури локальной области

# nonlocal -> позволяет изменять значение не локальной
# (замкнутой) переменной находясь внутри локальной области

# var = 100
# def increment(): # LEGB
#     global var
#     var += 1 

# print(var) # 100
# increment() # 101
# print(var)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment()
# print(counter())
# print(max)

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_wash = counter()
# c_ask = counter()
# # print(c) #function couner.<locals>.increment at...>
# print(c_wash()) #1
# print(c_wash()) #2
# print(c_wash()) #3
# print(c_wash()) #4
# print(c_wash()) #5
# print(c_ask())
# print(c_ask())

# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# globals - func которая возрващает все имена внутри глобальной области видимости

# local - функция которая возвращает все имена внутри глобальной области видимости и локальной

def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

def showStats(heroes, mobs):
    
    print()
    print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
    print()

counter_heroes = counter()
counter_mobs = counter()
heroes = 0
mobs = 0
print('Приветствую вас, вас король севера John Snow!')
while True:
    print('Тебе доступны следующие дейтсвия:')
    print('1-убить героя, 2-убить моба, 3-посмотреть статистику, 4-выйти из игры')
    choice = input('Введите что хотите сделать: ').strip()
    if choice == '1':
        heroes = counter_heroes()
        print('Вы обезглавили Ланистера!')
    elif choice == '2':
        mobs = counter_mobs()
        print('Вы убили белого ходока!')
    elif choice == '3':
        showStats(heroes, mobs)
    elif choice == '4':
        print('Пока пока! Ждем ещё раз!')
        break







