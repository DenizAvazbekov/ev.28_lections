# работе с файлами

# каретка - указатель - курсор

# open(<путь до файла>)

# file = open('/home/hello/Desktop/ev.28/lecture/files.py') # абсолютный путо
# file = open('files.py') # относительный путь
# (относительно той директории в которой вы работаете)

# Режим работы с файлами
# 1. Чтения -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавления -> a/a+ (append)
# b, x, t

# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# file = open('text.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# Контекстный менеджер
# with open('text.txt') as file: #file = open('text.txt)
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())
#     print(file, 'inside')

# print(file.read(), 'outside')

# file.tell() -> возрвращает индекс где находиться каретка
# (курсор)
# file.seek(index) -> перемещает курсор на индекс который вы передали

# with open('text.txt', 'r') as file:
    # print(file.readline().replace('\n', ''))
    # print(file.tell())
    # file.seek(0)
    # print(file.readline().replace('\n', ''))
    # data = file.read()
    # index = data.index('\n')
    # file.seek(index+1)i
    # print(file.readline().replace('\n', ''))
    # print(file.readline()[1].replace('\n', ''))
    # print(file.tell())
    # file.read()
    # file.seek(0)
    # print(file.tell())
    # print(file.readline())
    
# with open('text.txt' 'r') as file:
#     print(file.readline())
#     print(file.readlines(5))
#     print(file.read())

# with open('text.txt', 'a') as file:
#     file.write('Pervaya Strochka\n')
#     file.write('John Snow is bastard of Ned Stark!\n')
#     file.write('This is lesson about files!\n')
#     file.seek(0)
#     data = ['Bilal is genius!', 'Tima is good boy!']    
#     file.writelines(data)

# with open('text.txt', 'a+') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())

