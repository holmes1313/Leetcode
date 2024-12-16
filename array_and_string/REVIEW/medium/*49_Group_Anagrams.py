# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:37:40 2019

@author: z.chen7
"""

# 49. Group Anagrams
"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for value in strs:
            key = "".join(sorted(value))
            if key in ans:
                ans[key].append(value)
            else:
                ans[key] = [value]

        return list(ans.values())
        