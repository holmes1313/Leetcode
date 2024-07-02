# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:27:33 2019

@author: z.chen7
"""
# 15. 3Sum
"""
Given an array nums of n integers, are there elements a, b, c in nums such 
that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
        
        result = []
        nums.sort()
        
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        for i in range(len(nums)-2):
            # to avoid redundant current index
            # e.g. [-4, -1, -1, -, 1, , 2]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                
                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l += 1
                
                elif s > 0:
                    r -= 1
                  
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # to avoid redundant left/right index 
                    # e.g. [-2, 0, 0, 2, 2]
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                        
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                    
        return result


from typing import List


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1
            while left < right:
                sum3 = nums[left] + nums[right] + num
                if sum3 == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum3 > 0:
                    right -= 1
                else:
                    left += 1

        return ans

