# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:17:21 2019

@author: z.chen7
"""

# 414. Third Maximum Number
"""
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum."""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) >= 3:
            return sorted(set(nums), reverse=True)[2]
        
        else:
            return sorted(nums)[-1]


class Solution_2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = None
        max2 = None
        max3 = None
        
        for num in nums:
            
            if num in [max1, max2, max3]:
                continue
            
            if not max1 or num > max1:
                max1, max2, max3 = num, max1, max2
               
            elif not max2 or num > max2:
                max2, max3 = num, max2
                
            elif not max3 or num > max3:
                max3 = num
        
        return max3 if max3 is not None else max1