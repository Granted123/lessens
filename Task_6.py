x = int(input("Сколько денег в банке? "))
y = int(input("Какую сумму вы хотите получить? "))
P = int(input("Под сколько процентов вклад? "))
count_x = 0
year = 0
z = 0
while count_x < y:
    z = x * (P / 100)
    x += int(z)
    count_x = x
    year += 1
print(year)