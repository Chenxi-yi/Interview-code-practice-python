'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

'''
思路一：利用python自带的counter库

27ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        from collections import Counter
        # 返回一个列表，map（f,input）,对input进行f操作，第一个参数lambda函数，意思取返回值中的第一个数，因为counter函数返回的是字典，
        # counter（）.most_common返回的是有序的计数字段，去最后两个，顺序是从大到小的。
        return list(map(lambda c:c[0],Counter(array).most_common()[-2:]))

'''
思路二：异或运算
'''
'''
# 用的hashmap方法，返回[a,b] a是值，b是出现次数
        # hashmap就是字典，是无序的
        hashMap = {}
        # 把所有的数组里的单词转换成str然后放进字典
        for i in array:
            if str(i) in hashMap:
                hashMap[str(i)] += 1 # 如果已存在，那就加一
            else:
                hashMap[str(i)] = 1 # 如果没存在，就设为1
        # 查找为1的值
        res = []
        for k in hashMap.keys():
            if hashMap[k] == 1:
                res.append(int(k))
        return res
'''
