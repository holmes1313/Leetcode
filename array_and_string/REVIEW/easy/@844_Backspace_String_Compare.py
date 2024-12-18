# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:41:32 2019

@author: z.chen7
"""

# 844. Backspace String Compare
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.build_stack(s) == self.build_stack(t)

    def build_stack(self, s):
        stack = []
        for cha in s:
            if cha != "#":
                stack.append(cha)
            elif stack:
                stack.pop()

        return stack
