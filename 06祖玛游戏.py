#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/9
# @file 06祖玛游戏.py
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        import collections
        d = collections.defaultdict(int)
        for h in hand:
            d[h] += 1
        min_b :int = 6
        def d_b(s,t):
            nonlocal d
            nonlocal min_b
            n = len(s) - 1

            f :int = 1
            tt:int = 0
            while tt<n:
                if s[tt] == s[tt+1]:
                    f += 1
                else:
                    if f>2:
                        s = s[0:tt-f+1]+s[tt+1:]
                        tt -= f
                    f = 1
                tt+=1
                n = len(s) - 1

            n = len(s) - 1
            if n==0:
                if t<min_b:
                    min_b = t
            for i in range(n):
                if s[i] == s[i+1]:
                    f += 1
                else:
                    if f==1 and d[s[i]]>1:
                        d[s[i]] -= 2
                        d_b(s[0:i]+s[i+1:],t+2)
                        d[s[i]] += 2
                    elif f==2 and d[s[i]]>0:
                        d[s[i]] -= 1
                        d_b(s[0:i-1]+s[i+1:],t+1)
                        d[s[i]] += 1
                    # elif f>2:
                    #     d_b(s[0:i-f+1]+s[i+1:],t)
                    f = 1
        d_b(board+'a',0)
        if min_b == 6:
            return -1
        return  min_b

if __name__ == '__main__':
    s = Solution()
    print(s.findMinStep("WWRRBBWW","WRBRW"))