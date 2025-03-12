# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:57:29 2019

@author: z.chen7
"""

# 518. Coin Change 2
"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin. 

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10] 
Output: 1
"""
def coinChange(coins, amount, memo={}):
    
    if (amount, len(coins)) in memo:
        return memo[amount, len(coins)]
    
    if amount == 0:
        return 1
    
    if not coins:
        return 0
    
    coin = coins[-1]
    if coin == coins[0]:
        return 1 if amount % coin == 0 else 0
    
    numberOfWays = 0
    for cn in range(0, amount+1, coin):
        numberOfWays += coinChange(coins[:-1], amount-cn)
    memo[amount, len(coins)] = numberOfWays
    print(memo)    
    return numberOfWays


assert coinChange([1, 2, 5], 5)  == 5
assert coinChange([2], 3)  == 0
assert coinChange([10], 10) == 1
