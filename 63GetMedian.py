# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s = []

    def Insert(self, num):
        # write code here
        self.s.append(num)

    def GetMedian(self, s):
        # write code here
        self.s.sort()
        n = len(self.s)
        mid =n // 2
        if n%2 == 0:
            return (self.s[mid-1]+self.s[mid])/2.
        return self.s[mid]

