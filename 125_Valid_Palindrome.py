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
    

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            
            while l < r and not s[l].isalnum():
                l += 1
                
            while l < r and not s[r].isalnum():
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
                
