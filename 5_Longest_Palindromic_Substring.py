# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:05:35 2019

@author: z.chen7
"""
# 5. Longest Palindromic Substring
"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        res = s[0]
        for i in range(len(s)-1):
            # odd case, like "aba"
            odd = self.helper(s, i, i)
            # even case, like "abba"
            even = self.helper(s, i, i+1)
            res = max(res, odd, even, key=len)
            
        return res
        
    def helper(self, s, left, right):
        # starting at l,r expand outwards to find the biggest palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1: right]
        
        
        