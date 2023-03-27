educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
count = 0
one_month = expenses - educational_grant
print('1.месяц траты', expenses, 'не хватает', one_month)
for month in range(2, 11):
        inflation = expenses * 1.03
        duty = inflation - educational_grant
        count += duty + one_month
        print(month,'.месяц траты', expenses, 'не хватает', count)
        expenses = inflation
        one_month = 0
print('Нужно попросить у родителей', count, 'рублей')