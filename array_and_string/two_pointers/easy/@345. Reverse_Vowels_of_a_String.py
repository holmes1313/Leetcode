# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:30:32 2020

@author: z.chen7
"""

# 345. Reverse Vowels of a String
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -=1

        return "".join(s_list)
