# Операторы сравнения
# Условные операторы и логические операторы

# операторы сравнения
# <,>, ==(равно), !=(неравно), <=,>=

# 1 < 5 -> True 
# 7 < 9 -> False

# Условные операторы
# if
# elif
# else

# if <condition>:
#    <body if> # сработает если в condition if придет true
# [elif] <condition>
#     <body elif>
# [else]
#     <body else> # сработает если вы всех выше стоящих условиях пришло false

# string = input('Enter smt: ')

# if string.lower() == 'hello':
#     print('Hello, it\' me\nI was wondering if after all these years you\'d like to meet')
# elif string.lower() == 'john':
#     print('welcome back John Snow! The king of North ')
# elif string.lower() == 'abra-kadabra':
#     print('Sim Salamon Kadabra')
# else:
#     print('Совпадений не найдено!')

# print('Registration form:')
# email = input('Enter your email:')
# password = input ('Enter the password:')
# if len(password) < 8:
#      raise ValueError('Password is too short!\nNeed to be 8 symdols or more')
# elif password.isdigit():
#      raise ValueError('Password is invalid!\n Password must contain symbols too!')
# elif password.isalpha():
#      raise ValueError('Password is invalid!\nPassword must contain symbols too!')

# password2 = input('Enter password confirmation: ')

# if password != password2:
#      raise ValueError('Passwords did not match!')

# print(f'Successfully registered! Hello Mr/Mrs {email}')

 
# age =input('Enter your age: ')
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid Value for age!')

# if age <18:
#     print(f'Access Denied! Come again after {18 - age } year ')
# else:
#     print('You can pass! Welcome to KZ!')
    
# and - логическое и
# or -  лог или
# not - лог отрицание

# money = 100_000
# status = 'base'

# elif money > 1_000_000 or status == 'premium':
#     print('You\'are ministr of our club!')
# else:
#     print('You\'re honorable member of our club!')

# str1 = 'Hello world'
# print(str1)
# symbol = input('Enter the Symbol: ')


# age = 19
# user_coins = 11000

# if is_github_user or is_google_user and age > 21 or user_coins > 10000:
#     print(f'You can enter the system Mr/Mrs {user}!')
# else:
#     print('Sorry, you could not enter!')

# mark = int(input('vvedite chislo:')) 
# if mark >= 90: print("Отлично, Ваша оценка 5!") 
# elif mark >= 80 and mark < 90: 
#  print('Здорово, Ваша оценка 4!') 
# elif mark >= 70 and mark < 80: 
#  print('Хорошо, Ваша оценка 3!') 
# elif mark >= 60 and mark < 70: 
#  print('Вам стоит подучить материал') 
# else: print('Вы не сдали экзамен')
            

# string = int('fghjk:')
# if len(string) > 5:
#     print('True')
# else:
#     print('False')

# x = 32
# y = 32
# z = 100
# if x == y and y = z and x = z:
#     print('3')
# elif x == y or y == z or x == z:
#     print('2')
# else:
#     print('0')


















