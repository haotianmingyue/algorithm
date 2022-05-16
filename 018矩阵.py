#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/12/1
# @file 018矩阵.py
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[-1] * n for _ in range(m)]
        c: int = 0
        t: int = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    c += 1

        def change(i, j):
            nonlocal ans
            nonlocal c
            if i > -1 and i < m and j > -1 and j < n and ans[i][j] == -1:
                ans[i][j] = t + 1
                c += 1

        while c < m * n:
            for i in range(m):
                for j in range(n):
                    if ans[i][j] == t:
                        change(i - 1, j)
                        change(i + 1, j)
                        change(i, j - 1)
                        change(i, j + 1)
                        print(ans)
            t += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))