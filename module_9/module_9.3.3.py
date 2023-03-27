text = input('Введите текст: ')
firstsymbol = 0
secondsymbol = 0

for symbol in text:
    if symbol == 'ы':
        firstsymbol += 1
    if symbol == 'Ы':
        secondsymbol += 1

print('Больших букв Ы:', secondsymbol)
print('Маленьких букв Ы:', firstsymbol)
