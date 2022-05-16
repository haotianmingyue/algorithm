#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/19
# @file 012螺旋矩阵.py
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0]*n for _ in range(n)]
        # t :int = 1
        def write(i,j,p,nn):
            nonlocal ans
            if nn < n*n+1:
                if p == 'r':
                    while j < n and ans[i][j] == 0:
                        ans[i][j] = nn
                        j += 1
                        nn += 1
                    # print(ans)
                    write(i+1,j-1,'d',nn)
                elif p == 'd':
                    while i<n and ans[i][j] == 0:
                        ans[i][j] = nn
                        i += 1
                        nn += 1
                    # print(ans)
                    write(i-1,j-1,'l',nn)
                elif p == 'l':
                    while j>-1 and ans[i][j] == 0:
                        ans[i][j] = nn
                        j -= 1
                        nn += 1
                    # print(ans)
                    write(i-1,j+1,'u',nn)
                elif p == 'u':
                    while i>-1 and ans[i][j] == 0:
                        ans[i][j] = nn
                        i -= 1
                        nn += 1
                    # print(ans)
                    write(i+1,j+1,'r',nn)
        write(0,0,'r',1)
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(5))