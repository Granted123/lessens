number_of_debtors = int(input('Введите кол-во дожников: '))
count_duty = 0
for debtor in range(0, number_of_debtors, 5):
    print('Должник с номером ', debtor)
    duty = int(input('Сколько вы должны? '))
    count_duty += duty
print('Общая сумма долга:', count_duty)