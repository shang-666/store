import random

# 实现输入10个数字，并打印10个数的求和结果
# a = input().split()
# sum = 0
# for i in range(10):
#     sum += int(a[i])
# print(sum)

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# a = input().split()
# sum = 0
# for i in range(10):
#     sum += int(a[i])
# print(sum)
# print(max(a))
# print(sum/10)

# 使用random模块，如何产生 50~150之间的数？
# a = random.randint(50, 150)
# print(a)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。)
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b <= c or a-b >=c or a+c <= b or a-c >= b or b+c <= a or b-c >=a:
#     print('不能构成三角形')
# else:
#     if a == b == c:
#         print("等边三角形")
#     elif a == b or b == c or a == c:
#         print("等腰三角形")
#     elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
#         print("直角三角形")
#     else:
#         print("普通三角形")

# 有以下两个数，使用+，-号实现两个数的调换
# a = 5
# b = 10
# a = a+b
# b = a-b
# a = a-b
# print(a, b)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# i = 0
# while i < 3 :
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == "root" and password == "admin":
#         print("登录成功!")
#         break
#     else:
#         i += 1
#         if i == 3:
#             print("系统已锁定")

# 打印三角形
# 方法一
# n = int(input("请输入行数:"))
# for i in range(1, n+1):
#     print(" "*(n-i), end='')
#     for j in range(1, i+1):
#         print('* ', end='')
#     print('')
# 方法二
# line = 10
# for x in range(0, line):
#     print(" " * (line - x), end=" ")
#     print("* " * (x + 1))

# 使用while循环实现NxN乘法表的打印
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%dx%d=%d" % (i, j, i*j), end=' ')
#         j = j+1
#     print(' ')
#     i += 1

# 编程实现99乘法表的倒叙打印
# for i in range(9, 0, -1):
#     for j in range(1, i+1):
#         print("%d * %d = %d" %(j, i, i*j), end=' ')
#     print('')

# 一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# high = 0
# for i in range(1, 100):
#     high += 3
#     if high >= 20:
#         print("第%d天爬出来" % i)
#         break
#     high -= 2

# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
sum = 0
x = 1
for i in range(1, 21):
    x = x * i
    sum = sum + x
print(sum)
