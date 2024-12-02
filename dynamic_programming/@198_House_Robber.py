# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:06:21 2019

@author: z.chen7
"""

# 198. House Robber
"""
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security system connected and it will 
automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Input: [2,1,1,2]
Ouput: 4
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        def helper(nums):
            n = len(nums)
            if n == 0:
                return 0

            if n == 1:
                return nums[0]

            if n in memo:
                return memo[n]

            memo[n] = max(helper(nums[:-2])+nums[-1], helper(nums[:-1]))
            return memo[n]

        return helper(nums)


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        first = 0
        second = nums[0]
        for num in nums[1:]:
            curr = max(first + num, second)
            first = second
            second = curr

        return second
