print("Команды: exit - выход, play - начать игру")
print("БЫКИ И КОРОВЫ")
print("Правила игры:")
print("Компьютер загадал четырехзначное число. Вам нужно его отгадать. В числе цифры не могу повторятся и число не может начинаться с '0'.")
print("Если в введенном числе есть цифра не стоящая на своем месте, то компьютер выдаст вам кол-во таким цифр в качестве коров")
print("Аналогично происходит если вы ввели число и в нем есть цифра стоящая на своем месте, то компьютер выдаст вам их кол-во в качестве быков")
print("Пример игры:")
print("Загаданное число [6,2,3,1]")
print("1234 - 3 коровы")
print("5678 - 1 корова")
print("1256 - 2 коровы")
print("1236 - 4 коровы")
print("6213 - 2 быка 2 коровы")
print("6231 - 4 быка")
print("Вы ВЫИГРАЛИ!!!")
print("Удачной игры!")
from random import randint
global count, ai, repetition
count = 4
ai = True
repetition = False
def play():
    if ai:
        number = list()
        for i in range(0, count):
            if not repetition:
                while True:
                    e = str(randint(0, 9))
                    if not e in number:
                        break
            else:
                e = str(randint(0, 9))      
            number.append(e)
    else:
        number = list(input("Введите загадываемое число: "))
        if len(number) != count:
            print("Количество цифр в загадываемом числе не соответсвует настройкам!")
            return
        if repetition:
            for i in number:
                if number.count(i) > 1:
                    print("Цифра %s повторяется!" % i)
                    return
    game = True
    while game:
        numb = list(input("Введите число: "))
        if numb == ['e', 'x', 'i', 't']:
            print("Правильным числом было ", number)
            return
        if len(numb) != len(number):
            print("Количество цифр в вводимом числе не равно количетсву цифр в загадываемом числе!")
            continue
        cows = 0
        byki = 0
        for i in numb:
            try:
                if numb.index(i) == number.index(i):
                    byki = byki + 1
                else:
                    cows = cows + 1
            except ValueError:
                pass
        if byki == count:
            print("Вы угадали число!!!")
            return
        else:
            print("Коровы: {0}. Быки: {1}".format(cows, byki))
while True:
        word = input('Для начала игры введите "play"')
        print(' ')
        if word == "play":
            play()
        elif word == "exit":
            exit(0)  
        else:
            print("ERROR: command by name '%s' not found. Please try again" % word)




