desired_number = int(input("Загадайте число: "))
while True:
    number = int(input("Введите угадываемое число: "))
    if number > desired_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif number < desired_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали!!!")
        break
