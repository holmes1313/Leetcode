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
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtracking(curr, start):
            if len("".join(curr)) == len(s):
                result.append(curr[:])
                return

            for i in range(start, len(s)):
                partition = s[start: i+1]  # a, aa, aab
                if partition == partition[::-1]:
                    curr.append(partition)
                    backtracking(curr, i+1)
                    curr.pop()

        result = []
        backtracking([], 0)
        return result
