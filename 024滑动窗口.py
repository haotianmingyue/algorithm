#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/3/29
# @file 024滑动窗口.py
import queue
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def find_max(c):
            ans, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                if answerKey[right] == c:
                    sum += 1
                while sum > k:
                    if answerKey[left] != c:
                        left += 1
                        sum -= 1
                ans = max(ans, right - left + 1)
            return ans

        return max(find_max('T'), find_max('F'))

if __name__ == '__main__':
    s = Solution()
    print(s.maxConsecutiveAnswers("TTFTTTTTTFFTFTFTFFFTFFTTFTFTFFTTFTFTTTFTFTFTFFFFTTTTTTTFTFTFTFTFFTFTFTFTFTFFTFFFFFFFTTFFTFTFFTFTTFTFTFTT",8))