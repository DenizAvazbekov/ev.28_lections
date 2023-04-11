import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуйте угадать число.")

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Попытка №{}. Введите ваше число: ".format(tries+1)))
    tries += 1
    
    if guess < number:
        print("Мое число больше, попробуйте еще раз.")
    elif guess > number:
        print("Мое число меньше, попробуйте еще раз.")
    else:
        print("Поздравляю, вы угадали число за {} попыток!".format(tries))
        break
    