# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 22:50:18 2019

@author: z.chen7
"""

# 290. Word Pattern

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping1 = {}
        mapping2 = {}
        for p, w in zip(pattern, words):
            if p not in mapping1 and w not in mapping2:
                mapping1[p] = w
                mapping2[w] = p

            elif mapping1.get(p) != w or mapping2.get(w) != p:
                return False
        return True
