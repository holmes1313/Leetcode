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
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start+1, len(s)+1):
                substr = s[start: end]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])

        return result
        