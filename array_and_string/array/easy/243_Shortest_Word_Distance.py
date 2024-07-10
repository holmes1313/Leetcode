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

class Solution(object):
    def shortestDistance2(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word_index = {}
        min_distance = len(wordsDict)
        for idx, word in enumerate(wordsDict):
            if word == word1:
                word_index[word] = idx
                if word2 in word_index:
                    min_distance = min(min_distance, idx - word_index[word2])

            if word == word2:
                word_index[word] = idx
                if word1 in word_index:
                    min_distance = min(min_distance, idx - word_index[word1])

        return min_distance

    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = -1
        index2 = -1
        min_distance = float('inf')
        for idx, word in enumerate(wordsDict):
            if word == word1:
                index1 = idx
            elif word == word2:
                index2 = idx
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))

        return min_distance
