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
from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for b in range(len(prices)-1):
            for s in range(b+1, len(prices)):
                profit = max(prices[s] - prices[b], profit)

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i in range(1, len(prices)):
            maxprofit = max(prices[i] - minprice, maxprofit)
            minprice = min(prices[i], minprice)

        return maxprofit
        
        
    
    
 