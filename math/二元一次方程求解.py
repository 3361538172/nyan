print('例：ma + nb = p\n请依次输入一二组的m,n,p')
m1 = eval(input())
n1 = eval(input())
p1 = eval(input())
m2 = eval(input())
n2 = eval(input())
p2 = eval(input())
a = 0
b = 0
c = 0
 
c = m1/m2
b = (c * p2 - p1)/(c * n2 - n1)
a = (p1 - n1 * b)/m1

print (f'a = {a}, b = {b}')


