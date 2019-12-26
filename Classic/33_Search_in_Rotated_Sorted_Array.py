# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:41:22 2019

@author: z.chen7
"""
# 33. Search in Rotated Sorted Array
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:  # Found
                return mid
            if nums[low] < nums[mid]:  # Left is normally ordered
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:  # Right is normally ordered
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] == nums[mid]:  # search right
                    low = mid + 1
                else: #if nums[mid] == nums[high]:  # search left
                    high = mid - 1
        return -1
                

def test():
    output1 = Solution().search([1, 3], 2)         
    assert output1 == -1
    
    output2 = Solution().search([3, 1], 3)         
    assert output2 == 0