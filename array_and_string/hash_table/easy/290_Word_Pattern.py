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
        mapping = {}
        mapping2 = {}
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                mapping[pattern[i]] = s_list[i]
            else:
                if mapping[pattern[i]] != s_list[i]:
                    return False

            if s_list[i] not in mapping2:
                mapping2[s_list[i]] = pattern[i]
            else:
                if mapping2[s_list[i]] != pattern[i]:
                    return False

        return True
