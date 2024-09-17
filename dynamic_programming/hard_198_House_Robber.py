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
from typing import List
# odd elements list[1::2]         
# even elements list[0::2]        
# Top down dynamic programming (memoization) 


# for class, put memo in __init__
class Solution(object):
    def __init__(self):
         self.memo = {}
    def rob(self, nums):
        """
        :type nums: List(int)
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        if n not in self.memo:
            self.memo[n] = max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-1]))
        
        return self.memo[n]
    

# top down (memoization)
def rob_topDown(nums, memo={}):
    n = len(nums)
    if n == 0:     
        return 0    
    if n == 1:
        return nums[0]
    if n not in memo:
        memo[n] = max(rob_topDown(nums[:-2]) + nums[-1], rob_topDown(nums[:-1]))        
    return memo[n]


# bottom up - dynamic programing
class Solution_2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # prev1, prev2, num, ...
        curr = 0
        prev1 = 0
        prev2 = 0
        for num in nums:
            curr = max(num + prev1, prev2)
            prev1 = prev2
            prev2 = curr
        return curr