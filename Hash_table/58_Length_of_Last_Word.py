# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:55:41 2019

@author: z.chen7
"""

# 58. Length of Last Word
"""
Given a string s consists of upper/lower-case alphabets and empty space 
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        words = s.strip().split(" ")
        return len(words[-1])

    def lengthOfLastWord(self, s: str) -> int:
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1

        ans = 0
        while p >= 0 and s[p] != ' ':
            ans += 1
            p -= 1
        return ans
