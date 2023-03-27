a = int(input('Введите певое число: '))
b = int(input('Введите последнее число: '))
c = int(input('Введите делитель: '))
summ = 0
count = 0
for number in range(a, b):
    if number % c ==0:
        summ += number
        count += 1
print('среднее арифметическое всех чисел из '
      'отрезка [a; b], кратных числу c равно ', summ / count)
