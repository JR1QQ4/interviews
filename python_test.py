#!/usr/bin/python
# -*- coding:utf-8 -*-
# 统计在一个队列中的数字，有多少个正数，多少个负数，如 [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# pos_num = 0
# neg_num = 0
# for i in [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]:
#     if i > 0:
#         pos_num += 1
#     elif i < 0:
#         neg_num += 1
# print("大于 0 的个数：{}，小于 0 的个数：{}".format(pos_num, neg_num))

# 字符串 "axbyczdj"，如果得到结果“abcd“
# a = "axbyczdj"
# print(a[::2])
# print(''.join([a[i] for i in range(len(a)) if i % 2 == 0]))

# 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]
# a = "hello_world_yoyo"
# print(a.split('_'))

# 已知一个数字为 1，如何输出“0001”
# a = 1
# print("%04d" % a)

# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
# a = [1, 3, 5, 7]
# a.insert(3, a[0])
# print(a[1:])

# 已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9
# a = 9
# b = 8
# a, b = b, a
# print(a, b)

# 打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如： 153 是一个"水仙花数"，因为 153=1 的三次方＋ 5 的三次方＋ 3 的三次方。
# sxh = [i for i in range(100, 1000) if i == ((i // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 10) ** 3)]
# print(sxh)
# a = 153
# print(list(str(a)))

# 如果一个数恰好等于它的因子之和，则称该数为“完全数” ，又称完美数或完备数。
# 例如：第一个完全数是 6，它有约数 1、 2、 3、 6，除去它本身 6 外，其余 3 个数相加，
# 1+2+3=6。第二个完全数是 28，它有约数 1、 2、 4、 7、 14、 28，除去它本身 28
# 外，其余 5 个数相加， 1+2+4+7+14=28。那么问题来了，求 1000 以内的完全数有哪些？
# wqs = []
# for i in range(1, 1000):
#     s = 0
#     for j in range(1, i):
#         if i % j == 0 and j < i:
#             s += j
#     if s == i:
#         wqs.append(i)
# print(wqs)

# 用 python 写个冒泡排序
# import time
#
# a = [3, 1, 10, 9, 21, 35, 4, 6, 32, 54, 104, 234, 346, 23, 23, 22, 15, 38]
# s = range(1, len(a))[::-1]
# print(list(s))  # 交换次数
# start = time.time()
# for i in s:
#     for j in range(i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#     print("第 %s 轮交换后数据：%s" % (len(s) - i + 1, a))
# end = time.time()
# print(a)
# print('%.8f' % (end - start))
#
# a = [3, 1, 10, 9, 21, 35, 4, 6, 32, 54, 104, 234, 346, 23, 23, 22, 15, 38]
# l = len(a)
# start = time.time()
# for i in range(l):
#     for j in range(l - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# end = time.time()
# print(a)
# print('%.8f' % (end - start))

# 已知一个队列 [1, 3, 6, 9, 7, 3, 4, 6]
# 按从小到大排序; 按从大大小排序; 去除重复数字
# a = [1, 3, 6, 9, 7, 3, 4, 6]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# b = list(set(a))
# print(b)
# print(a)

# 计算 n!,例如 n=3(计算 321=6)， 求 10!
# from functools import reduce
# a = 10
# b = reduce(lambda x, y: x*y, range(1, a+1))
# print(b)
#
# def digui(n):
#     if n==1:
#         return 1
#     else:
#         return n * digui(n - 1)
# a = 10
# print(digui(a))

# 斐波那契数列，已知一个数列： 1、 1、 2、 3、 5、 8、 13、。。。。的规律为从 3 开始的每一项都
# 等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据
# a = 0
# b = 1
# while b < 100:
#     print(b)
#     a, b = b, a + b

# 幂的递归，计算 x 的 n 次方，如： 3 的 4 次方 为 3*3*3*3=81
# def mi(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * mi(x, n - 1)
# print(mi(3, 4))

# 汉诺塔问题，汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵
# 天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序
# 摞着 64 片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放
# 在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只
# 能移 动一个圆盘
# 当只有一个盘子的时候，只需要从将 A 塔上的一个盘子移到 C 塔上。
# 当 A 塔上有两个盘子是，先将 A 塔上的 1 号盘子（编号从上到下）移动到 B 塔上，
# 再将 A 塔上的 2 号盘子移动的 C 塔上，最后将 B 塔上的小盘子移动到 C 塔上。
# 当 A 塔上有 3 个盘子时，先将 A 塔上编号 1 至 2 的盘子（共 2 个）移动到 B 塔上
# （需借助 C 塔），然后将 A 塔上的 3 号最大的盘子移动到 C 塔，最后将 B 塔上的
# 两个盘子借助 A 塔移动到 C 塔上
# 当 A 塔上有 n 个盘子是，先将 A 塔上编号 1 至 n-1 的盘子（共 n-1 个）移动到 B
# 塔上（借助 C 塔），然后将 A 塔上最大的 n 号盘子移动到 C 塔上，最后将 B 塔上
# 的 n-1 个盘子借助 A 塔移动到 C 塔上
# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, '-->', c)
#         hanoi(n - 1, b, a, c)
# hanoi(3, 'A', 'B', 'C')

# 写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com），
# 程序识别用户名和公司名后，将用户名和公司名输出到控制台
# 1. 校验输入内容是否符合规范（xx@yy.com） , 如是进入下一步，如否则抛出提
# 示"incorrect email format"。注意必须以.com 结尾
# 2. 可以循环“输入--输出判断结果”这整个过程
# 3. 按字母 Q（不区分大小写） 退出循环，结束程序
# import re
# def is_mail_style(x):
#     a = re.match(r'^[0-9a-zA-Z\_\-]*@[0-9a-zA-Z]+(\.com)$', x)
#     if a:
#         yhm = re.findall(r"^(.+?)@", x)
#         print("用户名：%s" % yhm[0])
#         gc = re.findall(r"@(.+?)\.com", x)
#         print("公司名: %s" % gc[0])
#         return True
#     else:
#         print("incorrect email format")
#         return False
# a = input("请输入：")
# while 1:
#     if a == 'q' or a == 'Q':
#         exit()
#     else:
#         if is_mail_style(a):
#             break
#     a = input("请输入：")
# print("下一步！")

# 如何遍历查找出某个文件夹内所有的子文件呢？并且找出某个后缀的所有文件
# import os
# def get_files(path='C:\\ZZZZZ', rule=".py"):
#     all = []
#     for fpathe, dirs, fs in os.walk(path):  # os.walk 获取所有目录
#         print(fpathe, dirs, fs)
#         for f in fs:
#             filename = os.path.join(fpathe, f)
#             if filename.endswith(rule):  # 判断是否是”xxx“结尾
#                 all.append(filename)
#     return all
# print(get_files(path="C:\\ZZZZZZ\\all_test\\app_test"))
