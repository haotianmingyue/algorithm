#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/6
# @file 04动态规划_小偷.py
class Solution:
    def rob(self, nums: list[int]) -> int:
        ans = list()
        ans.append(0)
        ans.append(nums[0])
        for i in range(1,len(nums)):
            ans.append(max(ans[i],ans[i-1]+nums[i]))
        return max(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,9,9,9,2,3,1,4]))