a = eval(input('输入a：'))
b = eval(input('输入b：'))
c = eval(input('输入c：'))

sum_x = b/(-a)
product_x = c/a
_x = sum_x / 2
u = 0
x1 = 0
x2 = 0

if b**2 - 4*a*c >= 0:
    u = (_x**2 - product_x) ** 0.5
    x1 = _x + u
    x2 = _x - u
    print ('x1为%f\nx2为%f' %(x1, x2))
else:
    print ('无解')
