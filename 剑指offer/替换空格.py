'''
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

'''
方法1： 使用replace
24ms
5624k
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')


'''
方法二：当读取到‘ ’时，就直接加上'%20' 【这里是因为str是可以直接用+号相加而连起来，从而达到替换的效果】
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = ''
        for j in s:
            if j == ' ':
                new_s = new_s + '%20'
            else:
                new_s=new_s + j
        return new_s
