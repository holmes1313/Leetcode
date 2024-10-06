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
        # 1. find the longest non-increasing suffix
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # 2. check if nums are in descending order
        if i == 0:  
            nums.reverse()
            return
        
        # 3. identify pivot
        pivot = i - 1
        
        # 4. find rightmost successor to pivot in the suffix
        j = len(nums) - 1
        while nums[j] <= nums[pivot]:
            j -= 1
            
        # 5. swap with pivot
        nums[pivot], nums[j] = nums[j], nums[pivot]
        
        # 6. reserse the suffix
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        