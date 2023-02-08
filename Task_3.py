sum_bags = int(input("Сколько всего мешков? "))
count_bags = 0
sum_weight_bags = 0
while count_bags < sum_bags:
    weight_bag = int(input("Какой вес мешка?"))
    sum_weight_bags += weight_bag
    count_bags += 1
print("Общий вес мешков: ", sum_weight_bags)