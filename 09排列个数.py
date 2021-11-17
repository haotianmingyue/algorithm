#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/17
# @file 09排列个数.py
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        import collections
        d = collections.defaultdict(int)
        c: int = 0
        def find_all(n):
            nonlocal d
            nonlocal c
            if n == 0:
                c += 1
                return 1
            elif n > 0:
                t: int = 0
                for i in range(len(nums)):
                    if n - nums[i] in d:
                        c += d[n - nums[i]]
                        t += d[n - nums[i]]
                    else:
                        t += find_all(n - nums[i])
                d[n] = t
                return t
            else:
                return 0

        find_all(target)
        print(d)
        return c

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1,2,3,5,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],20))
    # print(2**32)
    # print(s.combinationSum4([1, 2, 3],4))