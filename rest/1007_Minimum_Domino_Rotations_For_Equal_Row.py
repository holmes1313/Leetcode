# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:59:40 2019

@author: z.chen7
"""

# 1007. Minimum Domino Rotations For Equal Row

"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, 
or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, 
as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252633/JavaPython-3-one-pass-counting-O(A-%2B-B)

import collections

class Solution:
    def minDominoRotations(self, A, B):
        
        countA = collections.Counter(A)
        countB = collections.Counter(B)
        countOverlapping = collections.Counter()
        
        for a, b in zip(A, B):
            if a == b:
                countOverlapping[a] += 1
                
        if len(countOverlapping) > 1:
            return -1
        
        for val in range(1, 7):
            if countA[val] + countB[val] - countOverlapping[val] == len(A):
                return min(countA[val], countB[val]) - countOverlapping[val]
            
        else:
            return -1