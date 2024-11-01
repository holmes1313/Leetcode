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

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for word in strs[1:]:
            n = min(len(prefix), len(word))
            j = 0
            while  j < n:
                if prefix[j] == word[j]:
                    j += 1
                else:
                    break
            prefix = prefix[:j]
            
            if prefix == "":
                return ""
        
        return prefix