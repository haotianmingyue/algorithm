#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/19
# @file 011整数替换.py
class Solution:
    def integerReplacement(self, n: int) -> int:
        # if n == 1:
        #     return 0
        # elif n&1 == 0:
        #     return self.integerReplacement(n//2) + 1
        # else:
        #     return 2 + min(self.integerReplacement(n//2),self.integerReplacement(n//2+1))
        c: int = 0
        # s = bin(n).replace('0b','')
        # i = len(s)-1
        while n > 1:
            while n & 1 == 0:
                n = n>>1
                c += 1
            if n == 3:
                c += 2
                break
            elif n & 3 == 3:
                n += 1
                c += 1
            elif n & 3 == 1:
                n -= 1
                c += 1
        return c




