# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:51:11 2020

@author: z.chen7
"""

"""
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

# 680. Valid Palindrome II

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True
            
    def isPalindrome(self, s):
        return s == s[::-1]