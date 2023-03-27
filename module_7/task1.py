count_number = 0
for count in range(10):
    number = int(input("Введите числа:"))
    if number % 2 == 0 and number > 0:
        count_number += 1
print(count_number)