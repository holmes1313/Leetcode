# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:07:42 2019

@author: z.chen7
"""

# 1137. N-th Tribonacci Number
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537"""

def tribonacci(n):
    memo = {}
    if n < 2:
        return n
    
    if n == 2:
        return 1
    
    if n not in memo:
        memo[n] = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
        
    return memo[n]

tribonacci(25)
