# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:03:14 2020

@author: z.chen7
"""

# 409. Longest Palindrome

"""
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # palindrome has one odd frequency element at most
        counter = collections.Counter(s)
        odds = 0
        for l, c in counter.items():
            if c % 2 == 1:
                odds += 1
                
        if odds > 1:
            return len(s) - (odds - 1)
        else:
            return len(s)


class Solution2:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)
        has_odd = False
        ans = 0
        for c in counts.values():
            if c % 2 == 0:
                ans += c
            else:
                ans += (c - 1)
                has_odd = True
        if has_odd:
            ans += 1
        return ans