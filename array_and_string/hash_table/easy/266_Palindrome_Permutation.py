# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:45:51 2019

@author: z.chen7
"""

# 266. Palindrome Permutation
"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # there's one odd-frequence element at most
        counter = collections.Counter(s)      
        odd = 0
        for c in counter.values():
            if c % 2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True
        