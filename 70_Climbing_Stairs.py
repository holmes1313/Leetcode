# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:41:15 2019

@author: z.chen7
"""

# 70. Climbing Stairs

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""


# self solution
# recursion with memoization
# memoized is outside the function 
memoized = {1: 1, 2: 2}
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    
    if n in memoized:
        return memoized[n]
    
    ways = climbStairs(n-1) + climbStairs(n-2)
    memoized[n] = ways
    
    return ways


# ansewer solution

def climbStairs_2(n):
    a = b = 1
    for i in range(n-1):
        a, b = b, a + b
    
    return b
    



    
climbStairs(35)    
climbStairs_2(35)    
memoized

len(range(1)  )  
    
    
    
    
    
    
    
    
    