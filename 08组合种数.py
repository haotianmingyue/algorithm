#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/17
# @file 08组合种数.py
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = list()
        l_t = list()
        if n > 9*k - (k-1)*k//2:
            return []
        def find_all(i,n_k,n_s):
            nonlocal l_t
            if n_k == k and n_s == n:
                ans.append(l_t[:])
            elif n_k < k:
                for j in range(i,10):
                    if j < 10:
                        l_t.append(j)
                        find_all(j+1,n_k+1,n_s+j)
                        l_t.pop()
        # for i in range(1,8):
        find_all(1,0,0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(9,24))