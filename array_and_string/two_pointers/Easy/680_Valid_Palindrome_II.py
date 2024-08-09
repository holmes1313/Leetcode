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

class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if s[p1] != s[p2]:
                #return self.isPalindrome1(s[p1:p2]) or self.isPalindrome1(s[p1+1:p2+1])
                return self.isPalindrome2(s, p1, p2-1) or self.isPalindrome2(s, p1+1, p2)

            p1 += 1
            p2 -= 1
        return True
    

    def isPalindrome1(self, s):
        return s == s[::-1]

    def isPalindrome2(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True
        