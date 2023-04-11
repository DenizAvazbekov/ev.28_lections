# Ternary operators(Тернарный оператор) - это конструкция
# которая по своему действию аналогична коннструкции if/else
# но при этом записывается в одну строку

# number = int(input('Vvedite chislo: '))
# res = 'even number' if number % 2 == 0 else 'odd number'
#     # четное                                    # нечетное
# print(res)

# <выражения если True> if <условие> else <выражения если False>

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max\min: ')

# res = max(ls) if choice.lower().strip() == 'max' else min             #1.
# (ls)
# print(res)

# if choice.lower().strip() == 'max':                                   #2.
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('Invalid choice!')

# res = max(ls) if choice.lower().strip() == 'max' else min             #3.
# (ls) if choice.lower().strip() == 'min' else 'invalid choice!'
# print(res)

#-----------------------------------------------------------------------------------
#calculator

# flag = True
# symbols = '0123456789' + '-' + '.'

# while flag:
#     num1 = input('Введите первое число: ')
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели неправильно число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#             continue
#     num2 = input('Введите второе число: ')
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели неправильно число!')
#             is_correct_number = False
#             break
#         if not is_correct_number:
#             continue

#     num1 = float(num1) if '.' in 
#     # print(num2, type(num2))
#     operator = input('Введите оператор(+, -, *, /): ')
#     if operator == '+':
#          print(f'Результат:{num1 + num2}')
#     elif operator == '-':
#          print(f'Результат:{num1 - num2}')
#     elif operator == '*':
#          print(f'Результат:{num1 * num2}')
#     elif operator == '/':
#          if num2 == 0:
#               print('На ноль делить нельзя')
#          else:
#               print(f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели неверный оператор!')
#     choice = input('Хотите продолжить(yes/no)?')
#     if choice.lower().strip() != 'yes':
#          flag = False
#          print('Пока!')




# phrase = "hello my name is john"
# words = phrase.split()  # Разделяем фразу на отдельные слова
# words.reverse()  # Изменяем порядок слов на обратный
# new_phrase = " ".join(words)  # Объединяем слова обратно в фразу
# print(new_phrase)  # Выводим перевернутую фразу









