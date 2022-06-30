#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/6/30
# @file 029计算质数个数——埃氏筛.py


"""
如果x是质数， 那么大于x的x的倍数 2x, 3x,...,一定不是质数。
如果从 2x开始标记是冗余的，应该直接从 x*x 开始。

首先 默认所有数都是质数， 从2开始（这样所有偶数都是0）， 大的奇数（不是质数）会有小奇数的因子。
"""
import math
import time


class Solution:
    def countPrimes(self, n: int) -> int:
        ans: int = 0
        mark = [1] * n
        if n == 0 or n == 1 or n == 2:
            return 0

        for i in range(2, n):
            if mark[i] == 1:
                ans += 1
                t = i * i
                while t < n:
                    mark[t] = 0
                    t += i
        return ans


if __name__ == '__main__':
    s = Solution()
    s_t = time.time()
    print(s.countPrimes(5000000), time.time() - s_t)











