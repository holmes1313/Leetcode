# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:14:49 2019

@author: z.chen7
"""

# 238. Product of Array Except Self
"""
Given an array nums of n integers where n > 1,  return an array output such 
that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        nums_copy = [1] + nums[:] + [1]
        left = right = 1
        for i in range(len(nums_copy) - 2):
            left = left * nums_copy[i]
            result.append(left)
            
        for i in range(len(nums_copy) - 1, 1, -1):
            right = right * nums_copy[i]
            result[i-2] *= right 
            
        return result
    
    
def test():
    input = [1,2,3,4]
    output = Solution().productExceptSelf(input)