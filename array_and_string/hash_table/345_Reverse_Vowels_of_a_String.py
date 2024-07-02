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
        l = 0 
        r = len(s) - 1
        ss = list(s)
        while l < r:
            if ss[l] in vowels and ss[r] in vowels:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
                
            elif ss[l] in vowels:
                r -= 1
            
            elif ss[r] in vowels:
                l += 1
                
            else:
                r -= 1
                l += 1
        
        return ''.join(ss)
                