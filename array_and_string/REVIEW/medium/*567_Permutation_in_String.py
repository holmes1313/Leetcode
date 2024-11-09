# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:58:39 2019

@author: z.chen7
"""
# 567. Permutation in String
"""
Given two strings s1 and s2, write a function to return true if s2 contains the 
permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""

# sliding window
# How do we know string word1 is a permutation of word2? collections.Counter(word1) == collections.Counter(word2) 
# we create a sliding window with length of s1, move from beginning to the end of s2. 
# When a character moves in from right of the window, we add 1 to that character count from the map. 
# When a character moves out from left of the window, we substruct 1 to that character count. 

import collections


class Solution(object):
    def checkInclusion(self, p, s):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        p_count = collections.Counter(p)
        window_count = collections.Counter()

        for i in range(len(s)):
            window_count[s[i]] += 1

            if i >= len(p):
                start_cha = s[i-len(p)]
                window_count[start_cha] -= 1
                if window_count[start_cha] == 0:
                    del window_count[start_cha]

            if window_count == p_count:
                return True

        return False