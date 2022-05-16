#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/20
# @file 015.py
class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        l = [0] * n
        ans = [0] * n
        tail = 0
        max_p: int = 0
        for i in range(len(rounds) - 1):
            s = rounds[i]
            e = rounds[i + 1]
            while s != e:
                l[s - 1] += 1
                s = (s + 1) % n
            l[s - 1] += 1
        print(l)
        for i in range(n):
            if l[i] > max_p:
                tail = 0
                ans[tail] = i + 1
                max_p = l[i]
            elif l[i] == max_p:
                tail += 1
                ans[tail] = i + 1
        return ans[:tail]


if __name__ == '__main__':
    # s = Solution()
    # print(s.mostVisited(4,[1,3,1,3]))
    print(2**31-1)