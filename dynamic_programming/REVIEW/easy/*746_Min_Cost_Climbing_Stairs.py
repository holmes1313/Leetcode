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


class Solution(object):

    # bottom-up (tabulation)
    def minCostClimbingStairs_bottomup(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        min_costs = [0] * (len(cost) + 1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, len(min_costs)):
            take_one_step = min_costs[i-1] + cost[i-1]
            take_two_step = min_costs[i-2] + cost[i-2]
            min_costs[i] = min(take_one_step, take_two_step)

        return min_costs[-1]

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def min_cost(n):
            if n <= 1:
                return 0

            if n not in cache:
                one_step = min_cost(n-1) + cost[n-1]
                two_step = min_cost(n-2) + cost[n-2]
                cache[n] = min(one_step, two_step)
            return cache[n]

        cache = {}
        return min_cost(len(cost))
            