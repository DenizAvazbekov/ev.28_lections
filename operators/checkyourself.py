"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def add_numbers(num1, num2):
#     num1 = int(input('vvedite 1 chislo: '))
#     num2 = int(input('vvedite 2 chislo: '))
#     result = num1 + num2
#     return result
# sum = add_numbers(5, 7)
# print(sum) 
"""
2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""
# def print_types(arg1, arg2):
#     print(f"The type of the first argument is {type(arg1)}")
#     print(f"The type of the second argument is {type(arg2)}")
# print_types(5, "Hello")
"""
3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""


"""
4) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
"""
#Пожалуйсте пишите текст на русском языке
# word = input('Vvedite tekst: ')
# Glasnyi = 0
# Soglasnyi = 0
# for i in word:
#     letter = i.lower()
#     if letter == "у" or letter == "е" or\
#        letter == "ы" or letter == "а" or\
#        letter == "о" or letter == "э" or\
#        letter == "я" or letter == "и" or\
#        letter == "ю":
#         Glasnyi += 1
#     else:
#         Soglasnyi += 1
# print("Glasnyi %i\nSoglasnyi %i" % (Glasnyi, Soglasnyi))

"""
5) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""

"""
6) Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.
"""
# def mul():
#     global num
#     num = num ** 2
#     return num
# num = 3

# for i in range(3):
#     mul()

# print(num) 
"""
7) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
main_doll_size = 10 # размер самой главной первой матрешки

def calculate_size():
    second_doll_size = 5
    def calculate_nested_size():
        third_doll_size = 3
        return main_doll_size + second_doll_size + third_doll_size
    return calculate_nested_size() + second_doll_size

total_size = calculate_size()
print(total_size) 

"""
8) Cоздайте переменную list_ и сохраните в ней список из чисел. Создайте новый список, используя встроенные функции, состоящий из квадратов этих чисел, результат сохраните в новой переменной result и выведите в консоль.

Обязатьльно нужно использовать builtin functions
"""

