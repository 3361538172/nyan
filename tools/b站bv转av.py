ten258 = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'

bv = input('请输入bv号：')    # BV1R7411y7kw
av = ''
count = 0
bvno = 2
av_list = []
count_list = []
sumbv = 0
sum_bv_pow = []

while bvno <=11:
    for count in list(range(0, 58)):
        if bv[bvno] == ten258[count]:
            av_list.append(ten258[count])
            count_list.append(count)
    bvno += 1
            
sum_bv_pow.append(count_list[0] * (58 ** 6))
sum_bv_pow.append(count_list[1] * (58 ** 2))
sum_bv_pow.append(count_list[2] * (58 ** 4))
sum_bv_pow.append(count_list[3] * (58 ** 8))
sum_bv_pow.append(count_list[4] * (58 ** 5))
sum_bv_pow.append(count_list[5] * (58 ** 9))
sum_bv_pow.append(count_list[6] * (58 ** 3))
sum_bv_pow.append(count_list[7] * (58 ** 7))
sum_bv_pow.append(count_list[8] * (58 ** 1))
sum_bv_pow.append(count_list[9] * (58 ** 0))

sumbv = sum(sum_bv_pow) - 100618342136696320

av = sumbv ^ 177451812

print ('av号为：\nav%d' %(av))
