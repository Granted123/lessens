positive_comment = 0
negative_comment = 0
while True:
    comment = int(input("Введите число: "))
    if comment == 0:
        break
    elif comment < 0:
        negative_comment += 1
    else:
        positive_comment += 1

print("Положительных комментариев:", positive_comment)
print("Отрицательный комментариев:", negative_comment)
