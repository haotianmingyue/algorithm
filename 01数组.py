#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/10/29
# @file 01数组.py
class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        arr.sort()
        import collections
        d = collections.defaultdict(int)
        for i in arr:
            d[i] += 1
        for k in d.keys():
            l_a = 0
            t = k
            while t in d.keys() and d[t] > 0:
                d[t] -= 1
                if t < 0:
                    t //= 2
                else:
                    t *= 2
                l_a += 1
                pass
            if l_a >= len(arr) // 2:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.canReorderDoubled([3,1,3,6]))

