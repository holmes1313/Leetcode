# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:49:07 2019

@author: z.chen7
"""

# 387. First Unique Character in a String
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

import collections

class Solution(object):
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        for l in s:
            if l not in mapping:
                mapping[l] = 1
            else:
                mapping[l] += 1

        for i in range(len(s)):
            if mapping[s[i]] == 1:
                return i

        return -1

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
                

