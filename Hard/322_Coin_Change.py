# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:25:59 2019

@author: z.chen7
"""

# 322. Coin Change
"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

# https://www.youtube.com/watch?v=1R0_7HqNaW0
"""
coins = [1,2,5]
amount = 11

dp[0] = 0
dp[1] = dp[1 - 1] + 1 = 1
dp[2] = min(dp[2-1] + 1, dp[2-2] + 1) = min(dp[1] + 1, dp[0] + 1) = `1
dp[3] = min(dp[3-1] + 1, dp[3-2] + 1) = min(dp[2] + 1, dp[1] + 1) = 2
...
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp
        # what is the smallest number of coins thet we need to make up for 0, 1, 2, ... amount
        coins.sort()
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a-c] + 1)
                else:
                    break
                    
        return dp[amount] if dp[amount] < amount+1 else -1 
            