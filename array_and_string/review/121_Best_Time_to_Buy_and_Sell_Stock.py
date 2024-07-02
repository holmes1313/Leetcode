# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:08:10 2019

@author: z.chen7
"""

# 121. Best Time to Buy and Sell Stock
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0."""

class Solution(object):
    # We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. 
    # Also, the second number (selling price) must be larger than the first one (buying price).
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for buy in range(len(prices) - 1):
            for sell in range(buy+1, len(prices)):
                max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)                # keep updating min price
            max_profit = max(max_profit, p - min_price)  # max profit = curr price - previous min price
        return max_profit            

        
    
 