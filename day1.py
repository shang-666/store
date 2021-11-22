yrf = [10, 69, 140, 10, 10]
nzk = [10, 72, 35, 90, 60, 60, 140]
fy = [43, 25, 43, 60, 43, 78]
pc = [63, 24, 63, 57]
t = [63, 45, 129, 63, 58, 48, 63]
cs = 120

sum_price = sum(yrf) * 253.6 + sum(nzk) * 86.3 + sum(fy) * 96.8 + sum(pc) * 135.9 + sum(t) * 65.8 + cs * 49.3
print('总销售额为:%.2f ' % sum_price)

sum1 = sum(yrf+nzk+fy+pc+t) + cs
avg = sum1 / 30
print('平均日销量:%.0f' % avg)

# 羽绒服销售量占比
a = sum(yrf)/sum1
print("羽绒服销量占比为:%.2f " % a)
# 牛仔裤销售量占比
b = sum(nzk)/sum1
print("牛仔裤销量占比为:%.2f " % b)
# 风衣销售量占比
c = sum(fy)/sum1
print("风衣销量占比为:%.2f " % c)
# 皮草销售量占比
d = sum(pc)/sum1
print("皮草销量占比为:%.2f " % d)
# T恤销售量占比
e = sum(t)/sum1
print("T恤销量占比为:%.2f " % e)
# 衬衫销售量占比
f = cs / sum1
print("衬衫销量占比为:%.2f " % f)

