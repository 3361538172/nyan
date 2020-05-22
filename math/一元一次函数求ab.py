x1 = eval(input('第一组的x：'))
y1 = eval(input('第一组的y：'))
x2 = eval(input('第二组的x：'))
y2 = eval(input('第二组的y：'))

a = 0
b = 0

if x1 == x2:
    ezit('两x需不同')
else:
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    print('a = %f, b = %f ' %(a, b))
