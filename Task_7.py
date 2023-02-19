N = int(input('Введите N: '))
summ = 0
for count in range(0, N):
    elem = ((-1) ** count) * 1 / 2 ** count
    summ += elem
print('Ответ:', summ)