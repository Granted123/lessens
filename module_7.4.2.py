number_1 = int(input("Введите первое число:"))
number_2 = int(input("Введите второе число:"))
summ_number = 0
for count in range(number_1, number_2+1):
    summ_number += count
print(summ_number)