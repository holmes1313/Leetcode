# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:30:08 2019

@author: z.chen7
"""
# 256. Paint House
"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10."""


# this is a case where only bottom up strategy works

# wrong answer !!
def minCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    memo = {}
    
    n = len(costs)
    
    if n == 0:
        memo[n] = 0
        return 0
    
    if n == 1:
        memo[n] = min(costs[0])
        return min(costs[0])
    
    if n not in memo:
        memo[n] = min((minCost(costs[:-2]) + costs[-2][0] + min(costs[-1][1], costs[-1][2])),
            (minCost(costs[:-2]) + costs[-2][1] + min(costs[-1][0], costs[-1][2])),
            (minCost(costs[:-2]) + costs[-2][2] + min(costs[-1][0], costs[-1][1])))
    
    return memo[n]


# correct answer
def minCost_dp(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    n = len(costs)
    
    if n == 0:
        return 0
    
    for i in range(1, n):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])
    
    return min(costs[-1][0], costs[-1][1], costs[-1][2])
    
minCost_dp([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]])
