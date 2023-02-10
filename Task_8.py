desired_number = int(input("Загадайте число от 1 до 100: "))
z = 0
count = 0
x = 1
y = 100
while z != desired_number:
    z = int(input("Ваше число: "))
    if z > desired_number:
        y = int((x+y)/2)
        print("Ваше число больше")
    elif z < desired_number:
        x = int((x + y) / 2)
        print("Ваше число меньше")
    count += 1
print("Вы угадали!!!",z)