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
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.helper(S) == self.helper(T)
    
    def helper(self, text):
        result = []
        for char in text:            
            if char != '#':
                result.append(char)            
            else:
                if result:
                    result.pop()
                else:
                    continue                    
        return result
                