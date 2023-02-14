number_of_students = int(input("Введите количество учеников: "))
excellent_student = 0
horoshist = 0
troechnik = 0
for grade in range(1, number_of_students + 1):
    List = int(input("Введите оценку ученика: "))
    if List == 5:
        excellent_student += 1
    elif List == 4:
        horoshist += 1
    else:
        troechnik += 1
if excellent_student > horoshist > troechnik:
    print("Отличников больше!!!")
elif excellent_student < horoshist > troechnik:
    print("Хорошистов больше!!!")
else:
    print("Троечников больше!!!")

