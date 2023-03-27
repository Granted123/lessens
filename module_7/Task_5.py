a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
count_number = 0
number = 0
factorial = 1
for count in range(a, b+1):
    if count % 3 == 0:
        number += count
        count_number += 1
print("среднее арифметическое всех чисел из "
      "отрезка [a; b], кратных числу 3 = ", number / count_number)