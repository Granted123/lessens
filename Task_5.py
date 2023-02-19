start_line  = int(input('Введите начало отрезка: '))
end_line = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
if start_line < 0 and step < 0:
    step *= -1
for count in range(start_line, end_line + 1, step):
    y = count ** 3 + 2 * count ** 2 - 4 * count + 1
    print('В точке', count, 'функция равна ', y)
