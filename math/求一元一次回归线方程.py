

your_i = int(input('一共有多少组数\n'))
xi = []
yi = []
xiyi = 0
xi_22 = 0
sum_xi = 0
sum_yi = 0
sum_xiyi = 0
p_x = 0
p_y = 0
p_x_22 = 0
p_xiyi = 0
a = 0
b = 0
in_count = 1
sqr_xi = []
xiyi_sum_list = []

while in_count <= your_i:
    x_i = float(input('第%d个x：' %(in_count)))
    y_i = float(input('第%d个y：' %(in_count)))
    xiyi = x_i * y_i
    xiyi_sum_list.append(xiyi)
    xi.append(x_i)
    yi.append(y_i)
    xi_22 = x_i ** 2
    sqr_xi.append(xi_22)
    in_count += 1

# xi，yi的平均数
sum_xi = float(sum(xi))
sum_yi = float(sum(yi))
p_x = float(sum_xi / your_i)
p_y = float(sum_yi / your_i)
p_x_22 = float(p_x ** 2)
p_xiyi = float(p_x * p_y)
xi_22 = float(sum(sqr_xi))
sum_xiyi = float(sum(xiyi_sum_list))

# 
b = float((sum_xiyi - your_i * p_xiyi)/(xi_22 - your_i * p_x_22))
a = float(p_y - b * p_x)

print ('a为%f，b为%f，方程为：y = %fx + %f' %(a, b, b, a))








