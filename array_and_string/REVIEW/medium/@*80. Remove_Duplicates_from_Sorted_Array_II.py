# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:04:52 2019

@author: z.chen7
"""

# 80. Remove Duplicates from Sorted Array II
"""
Given a sorted array nums, remove the duplicates in-place such that duplicates 
appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums 
being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:04:52 2019

@author: z.chen7
"""

# 80. Remove Duplicates from Sorted Array II
"""
Given a sorted array nums, remove the duplicates in-place such that duplicates 
appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums 
being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        next_idx = 1
        curr_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                curr_count += 1
            else:
                curr_count = 1

            if curr_count <= 2:
                nums[next_idx] = nums[i]
                next_idx += 1

        return next_idx

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nxt_idx = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[nxt_idx-1] or nums[i] != nums[nxt_idx-2]:
                nums[nxt_idx] = nums[i]
                nxt_idx += 1

        return nxt_idx
