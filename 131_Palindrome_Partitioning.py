# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:16:03 2019

@author: z.chen7
"""

# 131. Palindrome Partitioning
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        current = []
        start = 0
        self.backtrack(s, start, current, result)
        return result
    
    def backtrack(self, s, start, current, result):
        if start == len(s):
            result.append(current[:])
        else:
            for i in range(start, len(s)):
                partion = s[start:i+1]
                if partion == partion[::-1]:
                    current.append(s[start:i+1])
                    self.backtrack(s, i+1, current, result)
                    print current
                    current.pop()