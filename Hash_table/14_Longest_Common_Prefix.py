# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:15:03 2019

@author: z.chen7
"""

# 14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z."""

# get the shortest str in a list for common: min(strs, key=len)
# enumerate(str)

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    
    shortest = min(strs, key=len)
    
    for i, v in enumerate(shortest):
        for word in strs:
            if word[i] != v:
                return shortest[:i]
    else:
        return shortest
    
    
    
    
    
    
    
    
    