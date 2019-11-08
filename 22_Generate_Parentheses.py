# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:37:39 2019

@author: z.chen7
"""

# 22. Generate Parentheses

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        current = ""
        left = 0
        right = 0
        self.backtrack(current, left, right, n, result)
        return result
        
        
    def backtrack(self, current, left, right, n, result):
        if len(current) == n * 2:
            result.append(current)
            
        if left < n:
            self.backtrack(current+'(', left+1, right, n, result)
            
        if right < left:
            self.backtrack(current+')', left, right+1, n, result)
        
        
        
        
        
        
        
        
        
        
        
        
        