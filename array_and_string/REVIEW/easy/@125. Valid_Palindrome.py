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

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = "".join(cha.lower() for cha in s if cha.isalnum())
        return cleaned == cleaned[::-1]

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue

            if not s[p2].isalnum():
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                    return False
            else:
                p1 += 1
                p2 -= 1

        return True
