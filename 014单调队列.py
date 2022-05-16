#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/20
# @file 014单调队列.py
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = list()
        n = len(nums)
        q = [0]*len(nums)
        h = 0
        t = 0
        for i in range(k):
            if h==t:
                q[h] = nums[i]
                t = t+1
            else:
                while t>h and q[t-1]<nums[i]:
                    t = t-1
                q[t] = nums[i]
                t += 1
        ans.append(q[h])
        for i in range(k,n):
            if nums[i-k] == q[h]:
                h = h+1
            while t > h and q[t-1]<nums[i]:
                t = t-1
            q[t] = nums[i]
            t += 1
            ans.append(q[h])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7,4,1,3,7,8,9,1,2,4,431,342,2,4,5,6],3))