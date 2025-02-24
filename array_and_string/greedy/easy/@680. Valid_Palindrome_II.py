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

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left+1, right) or is_palindrome(left, right-1)
            left += 1
            right -= 1
        return True

        