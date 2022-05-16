#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/12/7
# @file 021旋转数组排序.py
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i: int = 0
        j: int = len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] < target:
                if nums[mid] > nums[j]:
                    i = mid + 1
                elif nums[mid] < nums[j]:
                    j = mid - 1
                else:
                    return j
            elif nums[mid] > target:
                if nums[mid] < nums[i]:
                    i = mid + 1
                elif nums[mid] > nums[i]:
                    j = mid - 1
                else:
                    return i
            else:
                return mid
        print(i,j)
        return i if -1 < i < len(nums) and nums[i] == target else -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,8,9,10,1,2,3],6))
