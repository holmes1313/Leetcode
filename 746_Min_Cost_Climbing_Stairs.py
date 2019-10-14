# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:13:03 2019

@author: z.chen7
"""
# un solved

# 746. Min Cost Climbing Stairs 
"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999]."""

def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """ 
    n = len(cost)
    memo = {}
    
    if n == 2:
        memo[n] = min(cost[0], cost[-1])
        return min(cost[0], cost[-1])
    
    if n == 3:
        memo[n] = min(cost[1], cost[0] + cost[2])
        return min(cost[1], cost[0] + cost[2])
    
    if n not in memo:
        memo[n] = min(minCostClimbingStairs(cost[:-1]), minCostClimbingStairs(cost[:-2])) + cost[-1]
    
    return memo[n]

test1 = [10, 15, 20]
test2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
minCostClimbingStairs(test1)
minCostClimbingStairs(test2)
