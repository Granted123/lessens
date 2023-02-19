reverse_timer = int(input('Введите время готовности: '))
for time in range(reverse_timer, 0, -1):
    print(time)
    eat = int(input('Готовы забрать еду(1 - да; 2 - нет):' ))
    if eat == 1:
        break
print('Ваша еда готова, осторожно горячo.')