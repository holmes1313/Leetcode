# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:45:52 2019

@author: z.chen7
"""

# 905. Sort Array By Parity
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        def f(a):
            return a % 2 != 0
        
        return sorted(A, key=f)
        """
        A_copy = A[:]
        left = 0
        right = len(A) - 1
        
        for a in A_copy:
            if a % 2 == 0:
                A[left] = a
                left += 1
            else:
                A[right] = a
                right -= 1
        
        return A








