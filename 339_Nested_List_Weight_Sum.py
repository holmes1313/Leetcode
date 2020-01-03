# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:11:26 2019

@author: z.chen7
"""
# 339. Nested List Weight Sum
"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.

Example 2:
Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth = 1
        result = []
        self.helper(nestedList, depth, result)
        return sum(result)
        
    def helper(self, nestedList, depth, result):
        for element in nestedList:
            if isinstance(element, list):
                self.helper(element, depth+1, result)
            elif isinstance(element, int):
                result.append(element * depth)


Solution().depthSum([[1,1],2,[1,1]])

Solution().depthSum([1,[4,[6]]])



class Solution_2(object):
    
    def __init__(self):
        self.result = 0
        
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth = 1
        self.helper(nestedList, depth)
        return self.result
        
    def helper(self, nestedList, depth):
        for element in nestedList:
            if isinstance(element, list):
                self.helper(element, depth+1)
            else:
                self.result += (element * depth)        
        
Solution_2().depthSum([[1,1],2,[1,1]])

Solution_2().depthSum([1,[4,[6]]])


