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
        if not nums:
            return -1
        
        # find the index of the smallest value using binary search
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        import pdb;pdb.set_trace()
        # now high == low is the index of the smallest value
        # also the index of rotated place
        # locate in which side the target is
        rot_index = low
        if target > nums[-1]:
            low = 0
            high = rot_index - 1
        else:
            low = rot_index
            high = len(nums) - 1
            
        # binary search
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

def test():
    output1 = Solution().search([1, 3], 2)         
    assert output1 == -1
    
    output2 = Solution().search([3, 1], 3)         
    assert output2 == 0