#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/5/23
# @file 025字符串表达式求值.py
# s = '3*2'
# print([i for i in range(1, 3, 2)])
# l = ['9', '*', '8']
# print(eval(str(l[0]+l[1]+l[2])))
# s = '99*88'
# print(list(s))
class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        ans = list()
        def find_all(s, j):
            if len(s) == 3:
                ans.append(eval(s[0]+s[1]+s[2]))
            else:
                for i in range(j, len(s), 2):
                    if i + 2 < len(s):
                        find_all(s[:i-1]+[str(eval(s[i-1]+s[i]+s[i+1]))]+s[i+2:], 1)
                    else:
                        find_all(s[:i - 1] + [str(eval(s[i - 1] + s[i] + s[i + 1]))], 1)

                    # find_all(s, j+2)
        expression_l = list()
        t = ''
        for i in range(len(expression)):
            if expression[i] not in ['*', '+', '-']:
                t += expression[i]
            else:
                expression_l.append(t)
                expression_l.append(expression[i])
                t = ''
        expression_l.append(t)
        find_all(expression_l, 1)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute("2*3-4*5"))