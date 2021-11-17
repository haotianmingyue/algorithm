#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/6
# @file 05找路径.py
class Solution:
    def pathWithObstacles(self, obstacleGrid: list[list[int]]) -> list[list[int]]:
        path = list()
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = list()
        v = [[0] * n for _ in range(m)]
        f: int = 0

        def find_path(i, j):
            nonlocal path
            nonlocal ans
            nonlocal f
            nonlocal v
            if i == m - 1 and j == n - 1 and obstacleGrid[i][j] == 0:
                v[i][j] = 1
                f = 1
                path.append([i, j])
                ans = path[0:]
            elif i < m and j < n:
                if obstacleGrid[i][j] == 0 and f == 0 and v[i][j] == 0:
                    v[i][j] = 1
                    path.append([i, j])
                    find_path(i + 1, j)
                    find_path(i, j + 1)
                    path.pop()

        find_path(0, 0)
        return ans

if __name__ == '__main__':
    s  = Solution()
    print(s.pathWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))