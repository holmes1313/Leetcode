# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:49:20 2019

@author: z.chen7
"""
# 448. Find All Numbers Disappeared in an Array
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                result.append(i)
        return result
