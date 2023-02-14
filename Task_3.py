n = int(input("Введите число: "))
factorial = 1
for count in range(1, n+1):
    factorial *= count
print(factorial)