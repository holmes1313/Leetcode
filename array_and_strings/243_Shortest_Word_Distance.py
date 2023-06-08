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


from typing import List


class Solution:
    def shortestDistance2(self, wordsDict: List[str], word1: str, word2: str) -> int:
        seen = {word1: [], word2: []}
        for i, word in enumerate(wordsDict):
            if word in seen:
                seen[word].append(i)
        smallest = len(wordsDict) - 1
        for i1 in seen[word1]:
            for i2 in seen[word2]:
                smallest = min(smallest, abs(i1 - i2))
        return smallest

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = i2 = -1
        output = len(wordsDict) - 1
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            else:
                continue

            if (i1 != -1) & (i2 != -1):
                output = min(output, abs(i1 - i2))

        return output
