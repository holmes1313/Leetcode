# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:09:00 2019

@author: z.chen7
"""

# 665. Non-decreasing Array
# ***
"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
"""

"""
The logic is to first find any inversions, and if the number of inversions is > 1, then we need to modify more than 1 element and hence we return False.

Once we find an inversion,

We have to fix either the current value or the next value appropriately so that any future inversions can be detected correctly.

Modification rule:

If you observe 20 30 10, we will find there is an inversion at 30 / 10. Because a[i-1] > a[i+1], we change a[i+1] to a[i]

If you observe 20 30 25, we will find there is an inversion at 30 / 25. Because a[i-1] < a[i+1], we change a[i] to a[i+1]
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1
                
                if i == 0:
                    nums[i] = nums[i+1]
                    
                elif nums[i-1] < nums[i+1]:
                        nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                
        return count <= 1
              
        