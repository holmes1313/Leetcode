# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:52:44 2019

@author: z.chen7
"""

# 28. Implement strStr()

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution:
    # sliding window
    def strStr2(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        for window_start in range(len(haystack) - len(needle) + 1):
            for i in range(len(needle)):
                if haystack[window_start + i] != needle[i]:
                    break
                if i == len(needle) - 1:
                    return window_start
        return -1



