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

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p1 = {}
        p2 = {}
        for i, val in enumerate(pattern):
            if val in p1:
                p1[val].append(i)
            else:
                p1[val] = [i]
                
        for i, val in enumerate(str.split()):
            if val in p2:
                p2[val].append(i)
            else:
                p2[val] = [i]
        
        return sorted(p1.values()) == sorted(p2.values())
    
    def wordPattern2(self, pattern, str):
        if len(pattern) != len(str.split()):
            return False
        d1, d2 = {}, {}
        for p, r in zip(pattern, str.split()):
            if p in d1:
                if d1[p] != r:
                    return False
            d1[p] = r
            if r in d2:
                if d2[r] != p:
                    return False
            d2[r] = p
        return True