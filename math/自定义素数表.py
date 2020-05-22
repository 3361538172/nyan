length = int(input('长度'))
list2 = range(1, length + 1)
count = 0

if count <= length:
    for y in list2:
        y_sqrt = y ** 0.5
        y_f = y_sqrt - int(y_sqrt)
        if y == 1 or (y == 2 or y == 5 or y == 7 or y == 3) and y_f != 0:
            print (y)
            count += 1
        elif y != 1 and y != 2 and y != 5 and y != 7 and y != 3:
            if y % 2 != 0 and y % 3 != 0 and y % 5 != 0 and y % 7 != 0 and y_f != 0:
                print (y)
                count += 1
            else:
                count += 1
