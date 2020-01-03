# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:32:45 2019

@author: z.chen7
"""

# 242. Valid Anagram
"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

import collections

def isAnagram(s, t):
    """
    :type s: str
    :type s: str
    :rtype: bool
    """
    return collections.Counter(s) == collections.Counter(t)


def isAnagram_sort(s, t):
    """
    :type s: str
    :type s: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
        
