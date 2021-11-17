#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/5
# @file 03最长等差序列.py
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        n = len(arr)
        max_l: int = 0
        import collections
        d = collections.defaultdict(int)
        d_v = {}
        for i in range(n):
            d[arr[i]] += 1

        def s_a(t):
            nonlocal d
            nonlocal d_v
            if t in d_v.keys():
                return d_v[t]
            elif t not in d.keys() or d[t] == 0:
                return 0
            else:
                d[t] -= 1
                l = s_a(t - difference)
                d_v[t] = l + 1
                return l + 1

        for i in range(n):
            if arr[i] not in d_v.keys():
                s_a(arr[i])
            if max_l < d_v[arr[i]]:
                max_l = d_v[arr[i]]
        return max_l

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubsequence([1,1,1,1,1,1,1,1],0))