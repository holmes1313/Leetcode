# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:09:20 2019

@author: z.chen7
"""

# 31. Next Permutation
"""
Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible 
order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding 
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        pivot = -1

        # find the pivot
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        # if not pivot, reserve the array
        if pivot == -1:
            nums.reverse()
            return

        # find the successor
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        # reverse the suffix
        nums[pivot+1: ] = reversed(nums[pivot+1: ])
        
        