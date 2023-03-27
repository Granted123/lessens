number = int(input("Введите число: "))
count_number = 0
sum_number = 0
while number != 0:
    count_number = number // 10
    number = count_number
    sum_number += 1
print(sum_number)