#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/23
# @file 016概率最大路径.py
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        v = [0] * n
        max_p = 0

        def find_m_p(s,p):
            nonlocal v
            nonlocal max_p
            if s == end:
                if p > max_p:
                    max_p = p
            else:
                for i in range(len(edges)):
                    if edges[i][0] == s and v[edges[i][1]] == 0:
                        v[edges[i][1]] = 1
                        find_m_p(edges[i][1],p *succProb[i])
                        v[edges[i][1]] = 0
                    elif edges[i][1] == s and v[edges[i][0]] == 0:
                        v[edges[i][0]] = 1
                        find_m_p(edges[i][0],p *succProb[i])
                        v[edges[i][0]] = 0
        v[start] = 1
        find_m_p(start,1)
        return max_p


if __name__ == '__main__':
    s = Solution()
    print(s.maxProbability(5,
[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],
[0.37,0.17,0.93,0.23,0.39,0.04],
3,
4))