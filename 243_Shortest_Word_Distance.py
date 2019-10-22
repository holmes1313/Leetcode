# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:17:24 2019

@author: z.chen7
"""

# 243. Shortest Word Distance
"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list."""

import collections

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        k = collections.defaultdict(list)
        for i, v in enumerate(words):
            k[v].append(i)
            
        min_d = len(words)
        
        for d1 in k[word1]:
            for d2 in k[word2]:
                if abs(d1 - d2) < min_d:
                    min_d = abs(d1 - d2)
                    
        return min_d
