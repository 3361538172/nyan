from random import choice
your_count = int(input('多少枚硬币'))
count = 1
list0 = []
list1 = []

while count <= your_count:
    side = choice([0, 1])
    if side == 0:
        list0.append(side)
    elif side == 1:
        list1.append(side)
    count += 1

length0 = len(list0)
length1 = len(list1)
print ('正面有%d枚，反面有%d枚' %(length1, length0))
