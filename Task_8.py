desired_number = int(input("Загадайте число от 1 до 100: "))
x = 50
y = 0
while True:
    number = print("Ваше число,", x, "? ")
    if number > y:

    elif number < y:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали!!!")
        break
