# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:22:41 2019

@author: z.chen7
"""

# 977. Squares of a Sorted Array
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""

class Solution(object):
class Solution(object):
    def sortedSquares2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result =  [num ** 2 for num in nums]
        result.sort()
        return result
        # return sorted(x*x for x in A)

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right] ** 2
                right -= 1
            else:
                square = nums[left] ** 2
                left += 1
            result = [square] + result

        return result

        