#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/17
# @file 09排列个数.py
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        c :int = 0
        ans = list()
        t_l = list()
        def find_all(t_n,t_s):
            if t_n == 0 and t_s == target:
                if t_l not in ans:
                    ans.append(t_l[:])
            elif t_n > 0 and t_s < target:
                for i in range(len(nums)):
                    t_l.append(nums[i])
                    find_all(t_n-1,t_s+nums[i])
                    t_l.pop()
        for i in range(1,target//min(nums)+1):
            find_all(i,0)
        print(ans)
        return len(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1,2,3,5,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],40))