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
        vowels = {"a", "e", "i", "o", "u"}
        p1 = 0
        p2 = len(s) - 1
        ans = [cha for cha in s]
        while p1 <= p2:
            if ans[p1].lower() in vowels and ans[p2].lower() in vowels:
                ans[p1], ans[p2] = ans[p2], ans[p1]
                p1 += 1
                p2 -= 1
            else:
                if ans[p1].lower() not in vowels:
                    p1 += 1
                if ans[p2].lower() not in vowels:
                    p2 -= 1
        return "".join(ans)
        
                