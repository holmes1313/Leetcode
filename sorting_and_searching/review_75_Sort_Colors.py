# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:24:02 2019

@author: z.chen7
"""

# 75. Sort Colors
"""
Given an array with n objects colored red, white or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite 
array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
import collections
from typing import List


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        nums[:count[0]] = [0] * count[0]
        nums[count[0]:count[0]+count[1]] = [1] * count[1]
        nums[count[0]+count[1]:] = [2] * count[2]


class Solution2_question:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        idx = 0
        while idx <= right:
            if nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                left += 1
            if nums[idx] == 2:
                nums[right], nums[idx] = nums[idx], nums[right]
                right -= 1
                idx -= 1
            idx += 1

        """
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]
            
            self.sortColors(L)
            self.sortColors(R)
            
            i = j = k = 0
            
            while (i < len(L)) and (j < len(R)):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                    
                k += 1
                
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
                
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
            """