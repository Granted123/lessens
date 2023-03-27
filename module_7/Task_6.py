for count in range(10, 100):
    one_number = count % 10
    two_number = count // 10
    product = one_number * two_number
    if product * 3 == count:
        print(count)