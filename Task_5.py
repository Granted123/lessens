hour = 1
count_wife = 0
count_job = 0
while hour < 9:
    job = int(input("Сколько задач решит максим? "))
    count_job += job
    wife = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if wife == 1:
        count_wife += 1
    hour += 1
print("Рабочий день закончился. Всего выполнено задач: ", count_job)
if count_wife != 0:
    print("Нужно зайти в магазин.")