num = int(input('输入数，判断是否为素数\n'))
num_s = num ** 0.5
num_f = num_s - int(num_s)

if num == 1 or (num == 2 or num == 5 or num == 7 or num == 3) and num_f != 0:
    print ('是素数')
elif num != 1 and num != 2 and num != 5 and num != 7 and num != 3 :
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num_f != 0:
        print ('是素数')
    else:
        print ('不是素数')
