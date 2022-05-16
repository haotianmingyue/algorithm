#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/12/7
# @file 020边界着色.py
class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        v = [[0]*n for _ in range(n)]
        def infection(i, j, c):
            nonlocal grid
            nonlocal  v
            if -1 < i < m and -1 < j < n:
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == c and v[i][j] == 0:
                    v[i][j] = 1
                    grid[i][j] = color
                    infection(i + 1, j, c)
                    infection(i - 1, j, c)
                    infection(i, j + 1, c)
                    infection(i, j - 1, c)
                    return 1
                elif grid[i][j] == c and v[i][j] == 0:
                    v[i][j] = 1
                    b_1 = infection(i + 1, j, c)
                    b_2 = infection(i - 1, j, c)
                    b_3 = infection(i, j + 1, c)
                    b_4 = infection(i, j - 1, c)
                    print(i, j, b_1, b_2, b_3, b_4)
                    if b_1 and b_2 and b_3 and b_4:
                        pass
                    else:
                        grid[i][j] = color
                    return 1
                elif v[i][j] == 1:
                    return 1
                else:
                    return 0
            return 0

        infection(row, col, grid[row][col])
        return grid

if __name__ == '__main__':
    s = Solution()
    print(s.colorBorder([[1,1,1],[1,1,1],[1,1,1]],1,1,2))