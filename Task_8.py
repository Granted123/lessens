desired_number = int(input("Загадайте число от 1 до 100: "))
x = int(input("Ваше число: "))
count = 1
while x != desired_number:
    if x > desired_number:
        x = int(x - x/2)
    elif x < desired_number:
        x = int(x / 2)
    count += 1
print(count)
print("Вы угадали!!!", x)
