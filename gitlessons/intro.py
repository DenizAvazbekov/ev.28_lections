# GIT - Распределенная система контроля версий
# это система для отслеживания и ведения истории изменения
# файлов, в вашем проекте. При помощи распределенности git 
# еще и организовывается командная работа

# Репозитрий - это хранилище вашего кода и истории его 
# изменение

# GitHub - веб сайт для размещение git-репозиториев в 
# совместной разработке проектов

# Команды Git:

# 1. git init - она создает новый локальный репозиторий, в 
# той директории в которой была прописана команда. (Команда
# вволится один раз в начале)

# 2. git add - команда для добавления изменений в систему
# отслеживания гита

# 3. git commit -m '<comment>' - команда для сохранения 
# всех изменений в локальном репозитории с комментарием к 
# ним

# 4. git remote add <origin> <url> - это команда для того 
# чтобы связать ваш локальный репо с удаленным репо в 
# гитхабе

# 5. git push <origin> <main> - команда отправки всех
# ваших изменений на удаленный репо

#---------------------------------------

# 1*) git init 
#         2) git add .
#         3) git commit -m ''
# 4*) git remote add origin <url>
#         5) git push origin main

#----------------------------------------
try:
    from PIL import Image
except ImportError:
     import Image

import pytesseract
import re

def get_imei_code(image):
    string = pytesseract.image_to_string(image)
    # print(string, type(string))
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    print(list_of_imei)

    with open('imei_codes.txt', 'w') as file:
        file.writelines(f'{x}\n' for x in list_of_imei)

image = 'imei.jpg'
get_imei_code(image)
#------------------------------------------


