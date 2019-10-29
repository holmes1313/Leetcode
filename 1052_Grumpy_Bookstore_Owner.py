# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:07:48 2019

@author: z.chen7
"""
# 1052. Grumpy Bookstore Owner

"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, 
some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy 
on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, 
the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for 
X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""

# https://leetcode.com/problems/grumpy-bookstore-owner/discuss/299284/Python-with-explanation.-Rolling-sum.

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        # The first involves counting how many customers are already satisfied
        # set any slots with already satisfied customers to 0
        # so that we will be left with only the currently unsatisfied customers in the list.
        already_satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        
        # find the subarray of length X that has the most customers
        # keep a rolling sum of the last X customers in the array
        best_k_minutes = 0
        current_k_minutes = 0
        
        #for i in range(len(customers) - X + 1):
            #best_k_minutes = max(best_k_minutes, sum(customers[i:i+X]))
        
        
        for i in range(len(customers)):
            current_k_minutes += customers[i]
            if i >= X:
                current_k_minutes -= customers[i-X]
            best_k_minutes = max(best_k_minutes, current_k_minutes)
            
        
        return already_satisfied + best_k_minutes
            