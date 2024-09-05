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


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        for window_start in range(m - n + 1):
            if haystack[window_start:window_start+n] == needle:
                return window_start

        return -1
        


