#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/17
# @file 010有序数组中单一元素.py
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        i: int = 0
        j: int = len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            print(mid)
            if mid & 1 == 0:
                if nums[mid] == nums[mid - 1]:
                    j = mid-1
                elif nums[mid] == nums[mid + 1]:
                    i = mid+1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    i = mid+1
                elif nums[mid] == nums[mid + 1]:
                    j = mid-1
                else:
                    return nums[mid]

        return nums[i]
if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([3,3,7,7,10,10,11,12,12,13,13,14,14]))