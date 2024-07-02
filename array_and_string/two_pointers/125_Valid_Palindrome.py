# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:50:57 2019

@author: z.chen7
"""


# 125. Valid Palindrome
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false"""

# alphanumeric characters  e.isalnum()

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True
    
    string_s = ''.join(e for e in s if e.isalnum()).lower()
    return string_s == string_s[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:

            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() != s[p2].lower():
                    return False
                else:
                    p1 += 1
                    p2 -= 1
            else:
                if not s[p1].isalnum():
                    p1 += 1

                if not s[p2].isalnum():
                    p2 -= 1

        return True