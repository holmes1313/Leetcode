# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:31:32 2019

@author: z.chen7
"""
# 862. Shortest Subarray with Sum at Least K

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = len(A) + 1
        cumu = [0] * (len(A) + 1)
        
        for i in range(len(A)):
            cumu[i+1] = cumu[i] + A[i]
            for j in range(i, -1, -1):
                if cumu[i+1] - cumu[j] >= K:
                    result = min(result, i+1 - j)
                    break
        return result if result <= len(A) else -1
    
    
Solution().shortestSubarray([2,-10,2,3], 4)
Solution().shortestSubarray([84, -37, 32, 40, 95], 167)
