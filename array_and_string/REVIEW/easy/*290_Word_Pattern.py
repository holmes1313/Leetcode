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
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p_to_s = {}
        s_to_p = {}
        s_list = s.split()
        p_list = list(pattern)
        
        if len(s_list) != len(p_list):
            return False

        for c1, c2 in zip(p_list, s_list):
            if (c1 not in p_to_s) and (c2 not in s_to_p):
                p_to_s[c1] = c2
                s_to_p[c2] = c1

            elif p_to_s.get(c1) != c2 or s_to_p.get(c2) != c1:
                return False

        return True
