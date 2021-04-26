#!/usr/bin/python
# -*- coding:utf-8 -*-
# 1.将给定的字符串，按照规则删除字符，输出删除后的字符串。删除规则为：相同字符连续，则删除，如”aaaab”删除后的字符串为”b” 。注：
# 仅是单个字符连续才删除，如babababa则不能删除
def del_str(input_str):
    while True:
        try:
            result = ""
            for i in range(len(input_str)):
                if len(input_str) == 1:
                    result = input_str
                    return result
                if i == 0:
                    if input_str[i + 1] != input_str[i]:
                        result += input_str[i]
                elif i == len(input_str) - 1:
                    if input_str[i - 1] != input_str[i]:
                        result += input_str[i]
                else:
                    if input_str[i - 1] != input_str[i] and input_str[i + 1] != input_str[i]:
                        result += input_str[i]
            if len(result) == 0:
                return "no"
            else:
                return result
        except:
            raise


# 2.小美和小团在玩一个游戏，小美任意给出一个大字符串str1以及一个独立的小字符串str2，小团需要从这个大字符串str1里找到包含独立小字符串
# str2中所有字符的最小子字符串str3；
# 例如，小美给出一个大字符串"meituan2019"和一个子字符串"i2t"，那么小团给出的答案就应该是"ituan2"；
# 需要注意：
# 1、str1中有可能没有完整包含str2所有字符的情况，此时返回""，即为空字符串；
# 2、str1不会为空，但str2有可能为空，此时返回整个str1；
# 3、str2可能存在重复的字符，此时str3需要包含相等数量该字符；
class Solution:
    @staticmethod
    def getMinString(str1, str2):
        if not str2:
            return str1
        min_index = len(str2)
        max_index = 0
        flag = 0
        str3 = list(str1).copy()
        for i in str2:
            if i in str3:
                flag += 1
                min_index = min(str3.index(i), min_index)
                max_index = max(str3.index(i), max_index)
                str3[str3.index(i)] = " "
        return str1[min_index:max_index + 1] if flag == len(str2) else ""


# 3.一个班级男生和女生数量相同，老师要求男生女生进行排队，男生全部排在队列前面，女生紧跟着排在男生队列后面，形成一个队列，现在要求
# 男生女生交叉排列并且第一位是男生，且每个人在在原队列中的顺序不变，如何来做？
# 要求：
# 交叉前：队列[男1，男2，男3，男4…男n，女1，女2，女3，女4…女n]
# 交叉后：队列[男1，女1，男2，女2，男3，女3，男4，女4…男n，女n]
def sort():
    while True:
        try:
            n = int(input())
            res = []
            for _ in range(2 * n):
                res.append(int(input()))
            for i in range(n):
                print(res[i])
                print(res[i + n])
        except:
            break
def sort2(n):
    boys = []
    girls = []
    result = []
    for i in range(1, n + 1):
        boys.append('男' + str(i))
        girls.append('女' + str(i))
    for i in range(n):
        result.append(boys[i])
        result.append(girls[i])
    return result


if __name__ == '__main__':
    print(del_str("babababa"))
    print(del_str("aaaab"))
    print(del_str("aaabbb"))
    print(Solution.getMinString("meituan2019", "i2t"))
    print(Solution.getMinString("aaabbc", "aab"))
    print(Solution.getMinString("abbcd", "bbc"))
    # sort()
    print(sort2(6))