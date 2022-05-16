#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/29
# @file 017字符串排列.py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n>len(s2):
            return False
        import collections
        d = collections.defaultdict(int)
        for c in s1:
            d[c] += 1
        s :int = 0
        e :int = 0
        for i in range(len(s2)):
            if e-s == n:
                return True
            else:
                if s2[i] not in d:
                    for j in range(s,i):
                        d[s2[j]] += 1
                    s = i+1
                    e = i+1
                else:
                    if d[s2[i]] > 0:
                        d[s2[i]] -= 1
                        e = i+1
                    else:
                        # if s2[s] == s2[i]:
                        #     s = s + 1
                        #     e = i+1
                        # else:
                        #     while s2[s] != s2[i]:
                        #         d[s2[s]] += 1
                        #         s += 1
                        while s2[s] != s2[i]:
                            d[s2[s]] += 1
                            s += 1
                        s += 1
            # if e-s > 550:
            #     print(s,e,e-s,n)
        return e-s == n

if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab","ba"))