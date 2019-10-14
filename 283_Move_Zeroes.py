# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:23:34 2019

@author: z.chen7
"""

# 283. Move Zeroes
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations."""


# self solution
# copy a list: nums_copy = nums[:]
# empty list conten: nums[:] = []

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype void Don't return anything, modify nums in-place instead
    """
    nums_copy = nums[:]
    nums[:] = []
    
    for num in nums_copy:
        if num != 0:
            nums.append(num)
    
    nums += [0] * (len(nums_copy) - len(nums))


# answer solution
def moveZeroes_2(nums):
    ZeroIndex = 0
    
    for i in range(len(nums)):
        # if current element is not 0, then we need to replace with with last 0 element
        if nums[i] != 0:
            nums[ZeroIndex], nums[i] = nums[i], nums[ZeroIndex]
            ZeroIndex += 1
            

# best answer
def moveZeros_3(nums):
    if not nums:
        return 
    
    i = 0
    
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1
            
    nums[i:] = [0] * (len(nums) - i)

test = [0,1,0,3,12]
moveZeros_3(test)
test
