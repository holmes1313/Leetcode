# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 16:52:33 2019

@author: z.chen7
"""

# 81. Search in Rotated Sorted Array II

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums = list(set(nums))
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2          
            if nums[mid] == target:
                return True
            
            while L < mid and nums[L] == nums[mid]:
                L += 1
            
            if nums[mid] <= nums[R]:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
                    
            elif nums[mid] > nums[L]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
                    
            else:
                while nums[mid] == nums[L]:
                    L = mid + 1
                while nums[mid]:
                    R = mid - 1
                    
        return False
                    