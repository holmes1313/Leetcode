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
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return [left + 1, right - 1]
        
        max_len = 0
        max_sub = ""
        for i in range(len(s)):
            odd_left, odd_right = expand_from_center(i, i)

            even_left, even_right = expand_from_center(i, i+1)

            if odd_right - odd_left + 1 > max_len:
                max_sub = s[odd_left: odd_right+1]
                max_len = odd_right - odd_left + 1

            if even_right - even_left + 1 > max_len:
                max_sub = s[even_left: even_right+1]
                max_len = even_right - even_left + 1
        
        return max_sub
