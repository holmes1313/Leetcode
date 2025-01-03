# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:42:41 2019

@author: z.chen7
"""

# 344. Reverse String
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory."""
s = ["h","e","l","l","o"]
s = s[::-1]
print(s)

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

        return s

