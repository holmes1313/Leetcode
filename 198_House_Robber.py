# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:06:21 2019

@author: z.chen7
"""

# 198. House Robber
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

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

# odd elements list[1::2]         
# even elements list[0::2]        
# Top down dynamic programming (memoization) 


def rob(nums):
    """
    :type nums: List(int)
    :rtype: int
    """
    memo = {}
    count = len(nums)
    
    if count == 0:
        memo[count] = 0
        return 0
    
    if count == 1:
        memo[count] = nums[count-1]
        return nums[count-1]
    
    if not memo.get(count):
        memo[count] = max(rob(nums[:-2]) + nums[count-1], rob(nums[:-1]))
    
    return memo[count]
    

rob([1,2,3,1]) 
rob([2,7,9,3,1])
rob([2,1,1,2])



def rob_2(nums):
    """
    :type nums: List(int)
    :rtype: int
    """
    prev = current = 0
    for num in nums:
        prev, current = current, max(prev + num, current)
        
    return current
        


# top down (memoization)
def rob_topDown(nums):
    n = len(nums)
    memo = {}
    
    if n == 0:
        #memo[n] = 0
        return 0
    
    if n == 1:
        #memo[n] = nums[0]
        return nums[0]

    if n not in memo:
        memo[n] = max(rob_topDown(nums[:-2]) + nums[-1], rob_topDown(nums[:-1]))
        
    return memo[n]

test1 = [2, 7, 9, 3, 1]
rob_topDown(test1)
len(test1)


# bottom up 
def rob_bottomUp(nums):
    n = len(nums)
    
    if n == 0:
        return 0
    
    a = 0
    b = nums[0]
    for i in range(1, n):
        b, a = max(a+nums[i], b), b
        
    return b