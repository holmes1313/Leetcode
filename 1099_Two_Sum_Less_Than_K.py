# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:14:19 2019

@author: z.chen7
"""

# 1099. Two Sum Less Than K
"""
Given an array A of integers and integer K, return the maximum S such that 
there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""

# binary search

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        left = 0
        right = len(A) - 1
        A.sort()
        while left < right:
            s = A[left] + A[right]    
            if s < K:
                result = max(result, s)
                left += 1
            else:
                right -= 1
        
        return result if result > 0 else -1
        