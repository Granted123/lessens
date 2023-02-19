all_buckwheat = 100
for time in range(1, 25):
    eat = int(input('Сколько раз за месяц вы питались? '))
    all_buckwheat -= 4 * eat
    print('К концу', time, 'месяца', 'осталось гречки:', all_buckwheat, 'кг')
