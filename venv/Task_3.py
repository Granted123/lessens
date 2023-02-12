winners = 0
for ticket in 345, 19, 955, 87, 421:
    if ticket % 5 == 0 and 99 < ticket < 1000:
        print('Счастливый билет', ticket)
        winners += 1
print(winners)