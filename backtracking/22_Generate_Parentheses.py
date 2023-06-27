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
from typing import List


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = right = n
        current = ''
        result = []
        self.dfs(left, right, current, result)
        return result
    
    def dfs(self, left, right, current, result):
        if left < 0 or right < left:
            return 
        
        if not left and not right:
            result.append(current)
        else:
            self.dfs(left-1, right, current + '(', result)
            self.dfs(left, right-1, current + ')', result)


class Solution_backtracking:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtracking(curr, left_count, right_count):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return

            if left_count < n:
                curr.append("(")
                backtracking(curr, left_count+1, right_count)
                curr.pop()

            if right_count < left_count:
                curr.append(")")
                backtracking(curr, left_count, right_count+1)
                curr.pop()

        ans = []
        backtracking([], 0, 0)
        return ans
        
        
