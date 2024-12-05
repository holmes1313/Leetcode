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
        if not needle:
            return -1

        m = len(haystack)
        n = len(needle)

        if m < n:
            return -1
    
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1
