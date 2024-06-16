# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:40:02 2019

@author: z.chen7
"""

# 205. Isomorphic Strings
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

# index distribution

import collections
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.helper(s) == self.helper(t)
        #return self.helper2(s) == self.helper2(t)
        
    def helper(self, word):
        result = collections.defaultdict(list)
        for i, v in enumerate(word):
            result[v].append(i)
            
        return sorted(result.values())
    
    def helper2(self, word):
        return [word.find(char) for char in word]


        return sorted(map1.values()) == sorted(map2.values())


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for c1, c2 in zip(s, t):
            if (c1 not in map1) and (c2 not in map2):
                map1[c1] = c2
                map2[c2] = c1

            else:
                if (map1.get(c1) != c2) or (map2.get(c2) != c1):
                    return False
        return True