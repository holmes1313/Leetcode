# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:17:24 2019

@author: z.chen7
"""

# 243. Shortest Word Distance
"""
Given a list of words and two words word1 and word2, 
return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list."""
class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_idx = None
        word2_idx = None
        shortest = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                word1_idx = i
                if word2_idx is not None:
                    shortest = min(shortest, i - word2_idx)

            elif word == word2:
                word2_idx = i
                if word1_idx is not None:
                    shortest = min(shortest, i - word1_idx)

        return shortest

