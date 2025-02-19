# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:54:59 2019

@author: z.chen7
"""

# 189. Rotate Array
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]"""

class Solution(object):        
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return nums

        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        return nums
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Reverse the whole array.
        #Reverse the first k elements to get them in their correct positions.
        #Reverse the remaining n - k elements to restore their order.
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k %= n
        if k > 0:
            reverse(nums, 0, n-1)
            reverse(nums, 0, k-1)
            reverse(nums, k, n-1)